import streamlit as st
from capaLogica.lReparacion import LReparacion

class PReparacion:
    def mostrar(self):
        st.subheader("Gestión de Reparaciones")

        lReparacion = LReparacion()
        id_tecnico = st.session_state["id_usuario"]

        # Formulario de registro
        st.markdown("### Registrar equipo")
        cliente = st.text_input("Cliente")
        equipo = st.text_input("Equipo (marca / modelo)")
        problema = st.text_area("Problema reportado")

        if st.button("Registrar reparación"):
            ok, codigo, mensaje = lReparacion.registrar(
                cliente, equipo, problema, id_tecnico
            )

            if ok:
                st.success(mensaje)
                st.info(f"Código de seguimiento: {codigo}")
                st.warning("Entregue este código al cliente")
            else:
                st.error(mensaje)
                
        # Lista de reparaciones
        st.markdown("### Mis reparaciones")
        reparaciones = lReparacion.listarPorTecnico(id_tecnico)

        if not reparaciones:
            st.info("No tienes reparaciones registradas")
            return

        for r in reparaciones:
            with st.expander(f"{r['equipo']} - {r['estado']}"):
                st.write(f"Cliente: {r['cliente']}")
                st.write(f"Problema: {r['problema']}")
                st.write(f"Fecha ingreso: {r['fecha_ingreso']}")

                nuevo_estado = st.selectbox(
                    "Actualizar estado",
                    ["RECIBIDO", "EN_REPARACION", "LISTO"],
                    index=["RECIBIDO", "EN_REPARACION", "LISTO"].index(r["estado"]),
                    key=f"estado_{r['id']}"
                )

                if st.button("Guardar estado", key=f"btn_{r['id']}"):
                    ok, msg = lReparacion.cambiarEstado(r["id"], nuevo_estado)
                    if ok:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
