import streamlit as st
from capaLogica.lVenta import LVenta
from capaLogica.lProducto import LProducto

class PVenta:
    def mostrar(self):
        st.subheader("Registrar Venta")

        productos = LProducto().listarProductos()

        if not productos:
            st.warning("No hay productos disponibles")
            return

        producto = st.selectbox("Producto",productos,format_func=lambda p: f"{p['nombre']} (Stock: {p['stock']})")

        cantidad = st.number_input("Cantidad", min_value=1, step=1)

        if st.button("Registrar venta"):
            ok, mensaje = LVenta().registrarVenta(st.session_state["id_usuario"],producto,cantidad)

            if ok:
                st.success(mensaje)
                st.rerun()
            else:
                st.error(mensaje)
