from capaDatos.dProducto import DProducto

class LProducto:
    def __init__(self, rol=None):
        self.__rol = rol
        self.__dProducto = DProducto()

    def listarProductos(self):
        # TODOS pueden listar
        return self.__dProducto.obtenerProductos()

    def crearProducto(self, data):
        if self.__rol != "ADMIN":
            raise PermissionError("Solo ADMIN puede crear productos")

        if not data["nombre"] or data["precio"] <= 0 or data["stock"] < 0:
            raise ValueError("Datos inválidos")

        return self.__dProducto.insertarProducto(data)

    def editarProducto(self, id_producto, data):
        if self.__rol != "ADMIN":
            raise PermissionError("Solo ADMIN puede editar productos")

        return self.__dProducto.actualizarProducto(id_producto, data)

    def eliminarProducto(self, id_producto):
        if self.__rol != "ADMIN":
            raise PermissionError("Solo ADMIN puede eliminar productos")

        return self.__dProducto.eliminarProducto(id_producto)
