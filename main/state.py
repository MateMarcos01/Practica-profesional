import reflex as rx
from main.dataBase.database import SessionLocal
from main.dataBase.models import Usuario
import bcrypt

class LoginState(rx.State):
    email: str = ""
    password: str = ""
    mensaje: str = ""

    def set_email(self, value: str):
        self.email = value

    def set_password(self, value: str):
        self.password = value

    def login(self):
        db = SessionLocal()

        try:
            user = db.query(Usuario).filter(
                Usuario.username == self.email
            ).first()

            if not user:
                self.mensaje = "Usuario no encontrado"
                return

            if not bcrypt.checkpw(self.password.encode('utf-8'), user.password.encode('utf-8')):
                self.mensaje = "Contraseña incorrecta"
                return

            self.mensaje = f"✅ Bienvenido {user.username}"
            self.email = ""
            self.password = ""

        except Exception as e:
            self.mensaje = f"Error: {e}"

        finally:
            db.close()


    def register(self):
        db = SessionLocal()

        try:
        # Verificar si ya existe
            user_exist = db.query(Usuario).filter(
            Usuario.username == self.email
            ).first()

            if user_exist:
                self.mensaje = "⚠️ El usuario ya existe"
                return

        # Crear nuevo usuario
            nuevo_usuario = Usuario(
                username=self.email,
                password=bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            )

            db.add(nuevo_usuario)
            db.commit()

            self.mensaje = "✅ Usuario registrado correctamente"
            self.email = ""
            self.password = ""

            return rx.redirect("/")

        except Exception as e:
            self.mensaje = f"Error: {e}"

        finally:    
            db.close()