import streamlit as st
from capaLogica.lReparacion import LReparacion

class PSeguimiento:
    def mostrar(self):
        st.subheader("Seguimiento de reparación")

        codigo = st.text_input("Ingrese su código de seguimiento")

        if st.button("Consultar"):
            reparacion = LReparacion().consultarPorCodigo(codigo)

            if reparacion:
                st.success("Reparación encontrada")
                st.write(f"Equipo: {reparacion['equipo']}")
                st.write(f"Estado: {reparacion['estado']}")
                st.write(f"Fecha ingreso: {reparacion['fecha_ingreso']}")
            else:
                st.error("Código no encontrado")
