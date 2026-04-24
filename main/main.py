import reflex as rx
from rxconfig import config
from main.pages.index import index
from main.pages.cursos import cursos
from main.components.navbar import navbar
from main.components.login import login
from main.pages.register import register



app = rx.App()
app.add_page(index, route="/")
app.add_page(cursos, route="/cursos")
app.add_page(register, route="/register")
