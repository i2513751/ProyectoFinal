from conexion import ConexionDB

class DUsuario:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()
        self.__tabla = 'usuarios'

    def obtenerUsuario(self, usuario):
        try:
            obUsuario = self.__db.table(self.__tabla).select('*').eq('usuario', usuario).execute()
            return obUsuario.data
        except Exception:
            return f'Error: '