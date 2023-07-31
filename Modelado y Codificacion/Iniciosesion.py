class InicioSesion:
    def __init__(self, usuarios_registrados):
        self.usuarios_registrados = usuarios_registrados

    def verificar_credenciales(self, usuario, contrasena):
        """Verifica si las credenciales son válidas para iniciar sesión."""
        if usuario in self.usuarios_registrados and self.usuarios_registrados [usuario]== contrasena:
            print(f"Bienvenido, {usuario}!")
            return True
        else:
            print("Credenciales incorrectas. Inténtalo nuevamente.")
            return False
