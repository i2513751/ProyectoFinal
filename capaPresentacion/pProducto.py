import streamlit as st
from capaLogica.lProducto import LProducto

class PProducto:
    def __init__(self):
        rol = st.session_state.get("rol")

        if rol != "ADMIN":
            st.error("Acceso restringido")
            st.stop()

        # Crear LProducto SOLO una vez y bien
        self.__lProducto = LProducto(rol)

    def mostrar(self):
        st.title("CRUD Productos (ADMIN)")

        # CREAR
        with st.form("crear_producto"):
            nombre = st.text_input("Nombre")
            precio = st.number_input("Precio", min_value=0.0)
            stock = st.number_input("Stock", min_value=0)
            guardar = st.form_submit_button("Guardar")

            if guardar:
                res = self.__lProducto.crearProducto({
                    "nombre": nombre,
                    "precio": precio,
                    "stock": stock
                })

                if res is True:
                    st.success("Producto creado")
                    st.rerun()
                else:
                    st.error(res)

        st.divider()

        # LISTAR / EDITAR / ELIMINAR
        st.subheader("Listado de productos")
        productos = self.__lProducto.listarProductos()

        if not productos:
            st.info("No hay productos registrados")
            return

        for p in productos:
            with st.expander(p["nombre"]):
                nombre = st.text_input(
                    "Nombre", p["nombre"], key=f"n{p['id']}"
                )
                precio = st.number_input(
                    "Precio", p["precio"], min_value=0.0, key=f"p{p['id']}"
                )
                stock = st.number_input(
                    "Stock", p["stock"], min_value=0, key=f"s{p['id']}"
                )

                col1, col2 = st.columns(2)

                if col1.button("Actualizar", key=f"u{p['id']}"):
                    res = self.__lProducto.editarProducto(
                        p["id"],
                        {"nombre": nombre, "precio": precio, "stock": stock}
                    )
                    if res is True:
                        st.success("Actualizado")
