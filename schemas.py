from pydantic import BaseModel
from typing import List
from typing import Annotated, Union

class FileBase(BaseModel):
    filename: str
    content_type: str
    data: bytes

class File(FileBase):
    class Config():
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class User(UserBase):
    id: int
    files: list[File] = []
    
    class Config():
        orm_mode = True

class ShowUser(User):
    name: str
    email:str
    blogs: List[File] = []
    class Config():
        orm_mode = True


