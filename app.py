import streamlit as st 
from PIL import Image

st.title("App1")

st.header("Este espacio es para el desarrollo de mis aplicaciones para Interfaces Multimodales.")
st.write("Fácilmente se realiza Back-End y Front-End.")
image = Image.open('Multimodal1.jpg')

st.image(image, caption='Interfaces Multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)

