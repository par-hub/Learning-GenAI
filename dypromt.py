import streamlit as st 
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
 
load_dotenv()  # Load environment variables from .env file 

st.title("Dynamic Prompt Generator")
role = st.selectbox("Select a role", ["AI Engineer", "Data Scientist", "Product Manager", "UX Designer"])
gole = st.text_input("Enter your goal")
context = st.text_area("Enter context (optional)")

template = PromptTemplate(template="You are a  senior {role} working in a company. Your goal is to {goal} and you have context {context}", input_variables=["role", "goal", "context"])
prompt = template.invoke({'role': role, 'goal': gole, 'context': context})

model = Ollama(model="gemma3:latest")

response = model.invoke(prompt)

if st.button("answerr"):
    st.write(response)

  