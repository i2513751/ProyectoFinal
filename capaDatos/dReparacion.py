from conexion import ConexionDB

class DReparacion:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()
        self.__tabla = "reparaciones"

    def registrarReparacion(self, cliente, equipo, problema, id_tecnico):
        reReparacion = self.__db.table(self.__tabla).insert({"cliente": cliente,"equipo": equipo,"problema": problema,"id_tecnico": id_tecnico}).execute()
        return reReparacion.data

    def listarReparacionesPorTecnico(self, id_tecnico):
        lisReparacion = (self.__db.table(self.__tabla).select("*").eq("id_tecnico", id_tecnico).order("fecha_ingreso", desc=True).execute())
        return lisReparacion.data

    def actualizarEstado(self, id_reparacion, nuevo_estado):
        self.__db.table(self.__tabla).update({"estado": nuevo_estado}).eq("id", id_reparacion).execute()
