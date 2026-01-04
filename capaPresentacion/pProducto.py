import streamlit as st
from capaLogica.lProducto import LProducto

class PProducto:
    def __init__(self):
        rol = st.session_state.get("rol")

        if rol not in ["ADMIN", "VENDEDOR", "TECNICO"]:
            st.error("Acceso restringido")
            st.stop()

        self.__lProducto = LProducto(rol)

    def mostrar(self):
        st.title("CRUD Productos (ADMIN)")

        # ================= CREAR =================
        with st.form("crear_producto"):
            nombre = st.text_input("Nombre")
            precio = st.number_input(
                "Precio",
                min_value=0.0,
                step=0.1
            )
            stock = st.number_input(
                "Stock",
                min_value=0,
                step=1
            )

            guardar = st.form_submit_button("Guardar")

            if guardar:
                res = self.__lProducto.crearProducto({
                    "nombre": nombre,
                    "precio": precio,
                    "stock": stock
                })

                if res is True:
                    st.success("Producto creado correctamente")
                    st.rerun()
                else:
                    st.error(res)

        st.divider()

        # ================= LISTAR =================
        st.subheader("Listado de productos")
        productos = self.__lProducto.listarProductos()

        if not productos:
            st.info("No hay productos registrados")
            return

        # ================= EDITAR / ELIMINAR =================
        for p in productos:
            with st.expander(p["nombre"]):
                nombre = st.text_input(
                    "Nombre",
                    value=p["nombre"],
                    key=f"n{p['id']}"
                )

                precio = st.number_input(
                    label="Precio",
                    min_value=0.0,
                    value=float(p["precio"]),
                    step=0.1,
                    key=f"p{p['id']}"
                )

                stock = st.number_input(
                    label="Stock",
                    min_value=0,
                    value=int(p["stock"]),
                    step=1,
                    key=f"s{p['id']}"
                )

                col1, col2 = st.columns(2)

                if col1.button("Actualizar", key=f"u{p['id']}"):
                    res = self.__lProducto.editarProducto(
                        p["id"],
                        {
                            "nombre": nombre,
                            "precio": precio,
                            "stock": stock
                        }
                    )
                    if res is True:
                        st.success("Producto actualizado")
                        st.rerun()
                    else:
                        st.error(res)

                if col2.button("Eliminar", key=f"d{p['id']}"):
                    res = self.__lProducto.eliminarProducto(p["id"])
                    if res is True:
                        st.warning("Producto eliminado")
                        st.rerun()
                    else:
                        st.error(res)
