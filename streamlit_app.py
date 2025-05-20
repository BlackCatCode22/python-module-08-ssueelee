import streamlit as st
from chatbot import ask_openai

st.title("Chatbot with Memory")

# Store messages in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        response = ask_openai(user_input)
        # Save to history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Show full chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
