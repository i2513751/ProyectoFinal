from capaDatos.dUsuario import DUsuario

class LUsuario:
    def __init__(self):
        self.__dUsuario = DUsuario()

    def validarLogin(self, usuario, password):
        data = self.__dUsuario.obtenerUsuario(usuario)

        if not data:
            return None

        user = data[0]

        if user["estado"] != "activo":
            return None

        if user["password"] != password:
            return None

        return user
