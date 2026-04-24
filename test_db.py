import sys
import os
from main.dataBase.database import SessionLocal
from main.dataBase.models import Usuario

try:
    db = SessionLocal()

    usuarios = db.query(Usuario).all()

    print("conexión exitosa a la base de datos")

    if not usuarios:
        print(u.username)

except Exception as e:
    print("Error:", e)
finally:
    db.close()