import streamlit as st
from capaLogica.lProducto import LProducto

class PProducto:
    def __init__(self):
        self.__lProducto = LProducto()
        self.construirInterfaz()

    def construirInterfaz(self):
        self.mostrarProducto()


    def mostrarProducto(self):
        st.subheader("Listado de productos")
        productos = self.__lProducto.listarProductos()
        st.dataframe(productos)

    def mostrar(self):

        if st.session_state.get("rol") != "ADMIN":
            st.error("Acceso restringido")
            st.stop()

        lp = LProducto(st.session_state["rol"])

        st.title("CRUD Productos")

        # CREAR
        with st.form("crear_producto"):
            nombre = st.text_input("Nombre")
            precio = st.number_input("Precio", min_value=0.0)
            stock = st.number_input("Stock", min_value=0)
            guardar = st.form_submit_button("Guardar")

            if guardar:
                res = lp.crearProducto({
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
        productos = lp.listarProductos()

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
                    res = lp.editarProducto(
                        p["id"],
                        {"nombre": nombre, "precio": precio, "stock": stock}
                    )
                    if res is True:
                        st.success("Actualizado")
                        st.rerun()
                    else:
                        st.error(res)

                if col2.button("Eliminar", key=f"d{p['id']}"):
                    res = lp.eliminarProducto(p["id"])
                    if res is True:
                        st.warning("Eliminado")
                        st.rerun()
                    else:
                        st.error(res)