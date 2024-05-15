from fastapi import FastAPI,HTTPException,status,UploadFile,File,Depends
from database import engine
import schemas,models
import save_file
from sqlalchemy.orm import Session
import database

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

get_db = database.get_db
    
@app.post("/save_file")
async def uploadfile(db: Session = Depends(get_db), file: UploadFile = File(...)):
    return await save_file.save_file(db,file)