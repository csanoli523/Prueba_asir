import streamlit as st

st.title("😈 Mi Nuevo App")
st.write("Esto es una prueba.")

st.header("Esto es una cabecera")

cantidad = st.slider("Elija un valor")

print(id(cantidad))

print(f' el identificador de cantidad es {id(cantidad)}')

for i in range(cantidad):
    st.button(f'Boton {i}')
    st.checkbox(f'Opcion {i}')
    