from dotenv import load_dotenv
import streamlit as st
import seaborn as sns
import pandas as pd
from langchain_openai import ChatOpenAI
from pandasai import SmartDataframe
import os

load_dotenv()

st.header('Mini-Assistente de Dados 🧠🐼', divider=True)

uploaded_file = st.sidebar.file_uploader(
    "Carregar CSV 📋", 
    type=['csv']
    )

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, sep=';')
    st.write(data.head(3))
else:
    st.warning("Por favor, insira um arquivo para análise. 📊")  

model = ChatOpenAI(model="gpt-3.5-turbo")

if "history" not in st.session_state:
    st.session_state.history = []

if uploaded_file is not None:
    df = SmartDataframe(data, config={"llm": model})
    prompt = st.text_area("Escreva Aqui")

    if st.button("Gerar"):
        if prompt:
            with st.spinner("Gerando Resposta..."):
                with st.chat_message("user"):
                     st.write(df.chat(prompt))

                image_folder = "<caminho-imagens-geradas>"
            try:

                files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.png')]
                
                files.sort(key=os.path.getmtime, reverse=True)

                latest_image = files[0]

                st.image(latest_image, caption="Imagem Gerada", use_container_width=True)
            except (IndexError, FileNotFoundError):
                st.error("Nenhuma imagem foi gerada ou a pasta não foi encontrada.")
