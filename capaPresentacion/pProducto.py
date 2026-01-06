import streamlit as st
from capaLogica.lProducto import LProducto

class PProducto:
    def mostrar(self):
        rol = st.session_state.get("rol")

        st.subheader("Productos")

        # LISTAR (todos los roles)
        productos = LProducto(rol).listarProductos()
        st.dataframe(productos)

        # SOLO ADMIN VE EL CRUD
        if rol != "ADMIN":
            return

        st.divider()
        st.title("Administrar productos")

        # CREAR
        with st.form("crear_producto"):
            nombre = st.text_input("Nombre")
            precio = st.number_input("Precio", min_value=0.0)
            stock = st.number_input("Stock", min_value=0)
            guardar = st.form_submit_button("Guardar")

            if guardar:
                try:
                    LProducto(rol).crearProducto({
                        "nombre": nombre,
                        "precio": precio,
                        "stock": stock
                    })
                    st.success("Producto creado")
                    st.rerun()
                except Exception as e:
                    st.error(e)

        st.divider()

        # LISTAR / EDITAR / ELIMINAR
        for p in productos:
            with st.expander(p["nombre"]):
                nombre = st.text_input("Nombre", p["nombre"], key=f"n{p['id']}")
                precio = st.number_input(
                    "Precio",
                    value=float(p["precio"]),
                    min_value=0.0,
                    key=f"p{p['id']}"
                )
                stock = st.number_input(
                    "Stock",
                    value=int(p["stock"]),
                    min_value=0,
                    key=f"s{p['id']}"
                )

                col1, col2 = st.columns(2)

                if col1.button("Actualizar", key=f"u{p['id']}"):
                    try:
                        LProducto(rol).editarProducto(
                            p["id"],
                            {"nombre": nombre, "precio": precio, "stock": stock}
                        )
                        st.success("Actualizado")
                        st.rerun()
                    except Exception as e:
                        st.error(e)

                if col2.button("Eliminar", key=f"d{p['id']}"):
                    try:
                        LProducto(rol).eliminarProducto(p["id"])
                        st.warning("Eliminado")
                        st.rerun()
                    except Exception as e:
                        st.error(e)
