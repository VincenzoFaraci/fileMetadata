from fastapi import FastAPI,HTTPException,status

app = FastAPI()

@app.get("/prova")
def prova(stringa: str):
    if stringa == "ciao":
        return stringa
    else:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)