import streamlit as st
from capaLogica.lUsuario import LUsuario

class PLogin:
    def mostrar(self):
        st.title("Login")

        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Ingresar"):
            user = LUsuario().validarLogin(usuario, password)

            if user:
                st.session_state["login"] = True
                st.session_state["id_usuario"] = user["id"]
                st.session_state["usuario"] = user["usuario"]
                st.session_state["rol"] = user["rol"]
                st.rerun()
            else:
                st.error("Credenciales inválidas")
