#  Q&A Chatbot
# from langchain_community.llms import OpenAI
from openai import OpenAI


from dotenv import load_dotenv

load_dotenv()

import os
import streamlit as st

## Load OpenAI model and get a response 

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def get_openai_response(question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question}
        ],
        temperature=0.6
    )

    return response.choices[0].message.content

    # llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name= 'gpt-4o', temperature=0.6)
    # response = llm(question)
    # return response

## Initialize Streamlit App
    
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Q & A App")

input_text = st.text_input("Input: ", key="input")
response = get_openai_response(input_text)

submit = st.button("Enter")


if submit:
    st.subheader("The response is")
    st.write(response)