from conexion import ConexionDB

class DVenta:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()

    def registrarVenta(self, id_vendedor, total):
        registrar = self.__db.table("ventas").insert({"id_vendedor": id_vendedor,"total": total}).execute()
        return registrar.data[0]  

    def registrarDetalle(self, id_venta, id_producto, cantidad, precio):
        self.__db.table("ventas_detalle").insert({"id_venta": id_venta,"id_producto": id_producto,"cantidad": cantidad,"precio": precio}).execute()

    def actualizarStock(self, id_producto, nuevo_stock):
        self.__db.table("productos").update({"stock": nuevo_stock}).eq("id", id_producto).execute()