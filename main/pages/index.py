import reflex as rx
from main.dataBase.database import SessionLocal
from main.dataBase.models import Usuario
from main.components.navbar import navbar
from main.components.login import login


def index():
    return login()






