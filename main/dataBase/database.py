from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:1234@localhost/campus_virtual"

engine = create_engine(
    DATABASE_URL,
    echo=True,  # Habilita el logging de SQL para depuración
    pool_pre_ping=True # Tamaño del pool de conexiones
)  

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()