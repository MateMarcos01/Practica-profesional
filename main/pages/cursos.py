import reflex as rx
from main.components.navbar import navbar

def cursos():
    return rx.vstack(
        navbar(),
        rx.text("Cursos", font_size=24, font_weight="bold"),
        padding="4",
    )