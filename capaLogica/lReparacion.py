from capaDatos.dReparacion import DReparacion

class LReparacion:
    def __init__(self):
        self.__dReparacion = DReparacion()

    def registrar(self, cliente, equipo, problema, id_tecnico):
        if not cliente or not equipo or not problema:
            return False, None, "Todos los campos son obligatorios"

        data = self.__dReparacion.registrarReparacion(cliente, equipo, problema, id_tecnico)

        codigo = data[0]["codigo"] 

        return True, codigo, "Reparación registrada correctamente"
    
    def listarPorTecnico(self, id_tecnico):
        return self.__dReparacion.listarReparacionesPorTecnico(id_tecnico)

    def cambiarEstado(self, id_reparacion, estado):
        if estado not in ["RECIBIDO", "EN_REPARACION", "LISTO"]:
            return False, "Estado inválido"

        self.__dReparacion.actualizarEstado(id_reparacion, estado)
        return True, "Estado actualizado"
    
    def consultarPorCodigo(self, codigo):
        codigo = codigo.strip().upper()

        if not codigo:
            return None

        data = self.__dReparacion.buscarPorCodigo(codigo)
        return data[0] if data else None

