import reflex as rx
from main.state import LoginState

def register():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Registro", size="6"),

                rx.input(
                    placeholder="Usuario",
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
                    "Registrarse",
                    on_click=LoginState.register,
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