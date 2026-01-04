from capaDatos.dProducto import DProducto

class LProducto:
    def __init__(self, rol):
        if rol not in ["ADMIN", "VENDEDOR", "TECNICO"]:
            raise PermissionError("No autorizado")


        self.__dProducto = DProducto()

    def listarProductos(self):
        return self.__dProducto.obtenerProductos()
    
    def crearProducto(self, data):
        if not data["nombre"] or data["precio"] <= 0 or data["stock"] < 0:
            raise ValueError("Datos inválidos")
        return self.__dProducto.insertarProducto(data)

    def editarProducto(self, id_producto, data):
        return self.__dProducto.actualizarProducto(id_producto, data)

    def eliminarProducto(self, id_producto):
        return self.__dProducto.eliminarProducto(id_producto)
