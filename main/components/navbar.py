import reflex as rx

def navbar():
    return rx.hstack(
        rx.text("Campus Virtual", font_weight="bold", font_size=20),
        rx.spacer(),
        rx.link("Inicio", href="/"),
        rx.link("Cursos", href="/cursos"),
        rx.link("Contacto", href="/contacto"),
        padding="2",
        bg="darkslategray",
        width="100%",
    )

