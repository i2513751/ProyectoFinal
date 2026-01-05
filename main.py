import streamlit as st
import streamlit as st

# 🔐 Inicialización OBLIGATORIA de sesión
if "login" not in st.session_state:
    st.session_state["login"] = False

if "rol" not in st.session_state:
    st.session_state["rol"] = ""

if "id_usuario" not in st.session_state:
    st.session_state["id_usuario"] = 0

from capaPresentacion.pLogin import PLogin
from capaPresentacion.pProducto import PProducto
from capaPresentacion.pVenta import PVenta
from capaPresentacion.pReparacion import PReparacion

if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    PLogin().mostrar()
else:
    st.write("Bienvenido")
    objetoPrueba = PProducto()

if st.session_state["rol"] == "VENDEDOR":
    PVenta().mostrar()
    
if st.session_state["rol"] == "VENDEDOR":
    PReparacion().mostrar()