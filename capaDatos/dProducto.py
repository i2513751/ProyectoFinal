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
            return f"Error: {e}"
        
    def insertarProducto(self, data):
        try:
            self.__db.table(self.__tabla).insert(data).execute()
            return True
        except Exception as e:
            return f"Error: {e}"

    def actualizarProducto(self, id_producto, data):
        try:
            self.__db.table(self.__tabla)\
                .update(data)\
                .eq("id", id_producto)\
                .execute()
            return True
        except Exception as e:
            return f"Error: {e}"

    def eliminarProducto(self, id_producto):
        try:
            self.__db.table(self.__tabla)\
                .delete()\
                .eq("id", id_producto)\
                .execute()
            return True
        except Exception as e:
            return f"Error: {e}"