import streamlit as st 
from PIL import Image

st.title("App1")

st.header("Este espacio es para el desarrollo de mis aplicaciones para Interfaces Multimodales.")
st.write("Fácilmente se realiza Back-End y Front-End.")
image = Image.open('Multimodal1.jpg')

st.image(image, caption='Interfaces Multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)

st.subheader("Ahora usamos 2 columnas")

col1, col2 = st.columns(2)

with col1: 
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales son versátiles y mejoran la experiencia del usuario")
  resp1 = st.checkbox('Estoy de acuerdo')
  resp2 = st.checkbox('No estoy de acuerdo')
  if resp1:
    st.write('Correcto!')
  if resp2:
    st.write('Incorrecto :(')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("¿Qué modalidad es la principal en tu interfaz?", ('Visual', 'Auditiva', 'Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz.')
  if modo == 'Auditiva':
    st.write('La audición es fundamental para tu interfaz.')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz.')
  
st.subheader("Uso de botones")
if st.button('Presiona el botón'):
  st.write('Gracias por presionarlo')
else:
  st.write('No has presionado aún')
  
st.subheader("Selectbox")
in_mod = st.selectbox(
  "Selecciona la modalidad",
  ("Audio", "Visual", "Háptico"),
)

if in_mod == "Audio":
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir video"
elif in_mod == "Háptico":
  set_mod = "Activar vibración"
st.write("La acción es:", set_mod)
