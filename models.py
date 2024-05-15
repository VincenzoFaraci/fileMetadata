from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)  
    
    items = relationship("File", back_populates="owner")

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    filename = Column(String)  # Aggiungi questa riga per la colonna filename
    content_type = Column(String)
    size = Column(Integer)
    data = Column(String)
    
    owner = relationship("User", back_populates="items")

