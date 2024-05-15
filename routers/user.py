from fastapi import APIRouter,Depends,status,HTTPException,Response
import database,schemas
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/user",
    tags=['user']
)

get_db = database.get_db()

@router.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
