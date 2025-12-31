from conexion import ConexionDB

class DProducto:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()
        self.__tabla = 'productos'
    

    def obtenerProductos(self):
        try: 
            listaProductos = self.__db.table(self.__tabla).select('*').execute()
            return listaProductos.data
        except Exception as e:
            return f'Error: '