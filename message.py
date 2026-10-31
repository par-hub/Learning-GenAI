from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama

message = [SystemMessage(content="you are a helpful assistant"), HumanMessage(content="What is the capital of France?")]

model = ChatOllama(model="gemma3:latest")
response = model.invoke(message)
print(response.content)