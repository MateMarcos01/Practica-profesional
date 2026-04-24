from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP

class Usuario(Base):
    __tablename__ = "usuarios"  #plural de usuario

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(100))