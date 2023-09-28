import streamlit as st
from PIL import Image

st.header('Augusto Nonato Moraes')

with st.chat_message("user"):
    st.write("Olá 👋, sou Graduando em Sistemas de informação pela Universidade Federal do Pará Campus Cametá e Utilizarei essa Biblioteca para desenvolver meu Trabalho"
             "de Conclusão de Curso (TCC)")
st.divider()

with st.container():
    image = Image.open('images/Augusto.jpeg')
    st.image(image,caption='Augusto Nonato Moraes', clamp=True)


result = st.button("Primeiro App")
if result:
    st.write('Obrigado por acessar a página!')