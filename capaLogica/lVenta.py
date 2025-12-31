from capaDatos.dVenta import DVenta
from capaDatos.dProducto import DProducto

class LVenta:
    def __init__(self):
        self.__dVenta = DVenta()
        self.__dProducto = DProducto()

    def registrarVenta(self, id_vendedor, producto, cantidad):
        if cantidad <= 0:
            return False, "Cantidad inválida"

        if cantidad > producto["stock"]:
            return False, "Stock insuficiente"

        total = producto["precio"] * cantidad

        venta = self.__dVenta.registrarVenta(id_vendedor, total)

        self.__dVenta.registrarDetalle(venta["id"],producto["id"],cantidad,producto["precio"])

        nuevo_stock = producto["stock"] - cantidad
        self.__dVenta.actualizarStock(producto["id"], nuevo_stock)

        return True, "Venta registrada correctamente"
