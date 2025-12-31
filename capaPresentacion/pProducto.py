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
