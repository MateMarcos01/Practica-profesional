import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Campus_Virtual.dataBase.database import SessionLocal
from Campus_Virtual.dataBase.models import Usuario

db = SessionLocal()

nuevo_usuario = Usuario(username="juan", password="1234")

db.add(nuevo_usuario)
db.commit()

print("Usuario insertado correctamente 🚀")

db.close()