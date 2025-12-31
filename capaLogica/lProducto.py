from capaDatos.dProducto import DProducto

class LProducto:
    def __init__(self):
        self.__dProducto = DProducto()

    def listarProductos(self):
        return self.__dProducto.obtenerProductos()