import streamlit as st

# 🔐 Inicialización de sesión
if "login" not in st.session_state:
    st.session_state["login"] = False

if "rol" not in st.session_state:
    st.session_state["rol"] = ""

if "id_usuario" not in st.session_state:
    st.session_state["id_usuario"] = 0

from capaPresentacion.pLogin import PLogin
from capaPresentacion.pProducto import PProducto
from capaPresentacion.pVenta import PVenta

# 🔐 LOGIN
if not st.session_state["login"]:
    PLogin().mostrar()
    st.stop()

# 🧪 DEBUG (puedes quitarlo luego)
st.write("ROL ACTUAL:", st.session_state["rol"])

st.title("Sistema de Ventas")
st.success("Bienvenido")

# 🛒 VENTAS → SOLO VENDEDOR
if st.session_state["rol"] == "VENDEDOR":
    PVenta().mostrar()
    PProducto().mostrar()


# 🛠 ADMIN (opcional, info extra)
if st.session_state["rol"] == "ADMIN":
    PProducto().mostrar()
    st.info("Panel de administración")
