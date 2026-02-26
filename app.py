import streamlit as st 
from PIL import Image

st.title("App1")

st.header("Este espacio es para el desarrollo de mis aplicaciones para Interfaces Multimodales.")
st.write("Fácilmente se realiza Back-End y Front-End.")
image = Image.open('Multimodal1.jpg')

st.image(image, caption='Interfaces Multimodales')
