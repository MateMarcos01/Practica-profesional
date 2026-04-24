import reflex as rx
from main.state import LoginState

def login():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Iniciar Sesión", size="6"),

                rx.input(
                    placeholder="Correo",
                    value=LoginState.email,
                    on_change=LoginState.set_email,
                ),

                rx.input(
                    placeholder="Contraseña",
                    type_="password",
                    value=LoginState.password,
                    on_change=LoginState.set_password,
                ),

                rx.button(
                    "Ingresar",
                    on_click=LoginState.login,
                ),

                rx.link(
                    "¿No tienes cuenta? Regístrate",
                    href="/register",
                    color="blue",
                    font_size="0.9em",
                ),

                rx.text(LoginState.mensaje),

                spacing="4",
            ),
            padding="2em",
            bg="white",
            border_radius="10px",
            width="350px",
        ),
        height="100vh",
        bg="gray.100",
    )