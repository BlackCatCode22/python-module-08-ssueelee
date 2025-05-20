import openai
import streamlit as st

# Load the key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

def ask_openai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content.strip()
