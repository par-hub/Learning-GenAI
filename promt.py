
import streamlit as st

from langchain_community.llms import Ollama

st.title("Static Prompt Generator")

inputi = st.text_input("Enter your question")

model = Ollama(model="gemma3:latest")

if st.button("Generate Prompt"):
    if inputi:
        response = model.invoke(inputi)
        st.write("Response:", response)
    else:
        st.warning("Please enter a question.")
 
