from fastapi import UploadFile, File
from sqlalchemy.orm import Session
import schemas,models,io,json,tempfile,os
from fastapi import HTTPException,status
from PIL import Image, ExifTags,TiffImagePlugin
from PIL.ExifTags import TAGS




"""async def save_file(request: schemas.File, db: Session,file: UploadFile = File(...)):
    contents = await file.read()
    new_file = models.File(filename = request.filename, content_type = request.content_type, data = contents)
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return new_file"""

async def save_file(db: Session, file: UploadFile = File(...)):
    #return "hello" ok
    if file.content_type.startswith("image"):
        #return "hellod"
        return await save_image(db,file)
    elif file.content_type.startswith("text"):
        #return "ciao"
        return await save_text(db,file)
    elif file.content_type.startswith("video"):
        return await save_video(db,file)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    

async def save_text(db: Session, file: UploadFile = File(...)):
    contents = await file.read()
    text_length = len(contents)
    new_file = models.File(
        filename=file.filename, 
        content_type=file.content_type,
        size=len(contents), #da sistemare
        data=contents,
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return new_file
    
    

async def save_image(db: Session, file: UploadFile = File(...)):
    contents = await file.read()  # Leggi il contenuto del file
    img = Image.open(io.BytesIO(contents))
    exif_info = img._getexif()
    exif = {}
    for k, v in img._getexif().items():
        if k in ExifTags.TAGS:
            v = cast(v)
            exif[ExifTags.TAGS[k]] = v

    # Serializza il dizionario exif in una stringa JSON
    data_str = json.dumps(exif)

    # Crea un nuovo oggetto File e aggiungilo al database
    new_file = models.File(
        filename=file.filename, 
        content_type=file.content_type,
        size=len(contents),  # Dimensione effettiva del file in byte
        data=data_str,
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return new_file


async def save_video(db: Session, file: UploadFile = File(...)):
    pass


def cast(v):
    if isinstance(v, TiffImagePlugin.IFDRational):
        if v.denominator != 0:
            return float(v.numerator) / float(v.denominator)
        else:
            return None  # o un valore predefinito, a seconda del caso
    elif isinstance(v, tuple):
        return tuple(cast(t) for t in v)
    elif isinstance(v, bytes):
        return v.decode(errors="replace")
    elif isinstance(v, dict):
        for kk, vv in v.items():
            v[kk] = cast(vv)
        return v
    else: 
        return v