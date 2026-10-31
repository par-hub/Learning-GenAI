import streamlit as st
from dotenv import load_dotenv
from langchain_community.llms import Ollama


load_dotenv()  # Load environment variables from .env file  

st.title("Google Gemma")
input_text = st.text_input("Enter your question")
model = Ollama(model="gemma3:latest")

if input_text:
    response = model.invoke(input_text)
    st.write("Response:", response)