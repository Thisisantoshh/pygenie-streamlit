import streamlit as st
import requests

st.set_page_config(page_title="PyGenie Chat", page_icon="🐍")
st.title("🤖 Chat with PyGenie - Your Python Assistant")

user_input = st.text_input("Ask me a Python question:")

if user_input:
    with st.spinner("Thinking..."):
        response = requests.post(
            "https://huggingface.co/chat/assistant/684d449e90ff70b7cecdbaab",
            json={"inputs": user_input}
        )
        if response.status_code == 200:
            reply = response.json().get("generated_text", "No response received.")
        else:
            reply = "Something went wrong. Please try again."

        st.markdown("### PyGenie says:")
        st.success(reply)
