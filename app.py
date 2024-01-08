from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv() #will load variables from .env-------here we load the openAI api-key

# Function to load OpenAI model 

def get_responses(question):
    llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'), model = 'text-davinci-003', temperature = 0.6)
    response = llm(question)
    return response
# streamlit app
    
st.set_page_config(page_title='My ChatBot')
st.header('OpenAI gpt-3.5-turbo model')

input = st.text_input('Input: ', key='input')
response = get_responses(input)

submit = st.button('Ask me anything')

# now if query button gets clicked:
if submit:
    st.subheader('Answer:')
    st.write(response)
