import streamlit as st
from capaLogica.lPersona import LPersona

class PPersona:
    def __init__(self):
        self.__lPersona = LPersona()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.button('🛒')
        st.title('Bienvenidos')
        with st.container():
            st.write('Cargador ')
            st.image('file.jpg', width='content' )
            st.button('Agregar', type='primary', width='content')
        self.mostrarPersona()
    


    def mostrarPersona(self):
        listaPersonas = self.__lPersona.mostrarPersona()
        st.dataframe(listaPersonas)


