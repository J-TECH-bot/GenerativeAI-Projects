from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
#load api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini pro model
model = genai.GenerativeModel("gemini-pro")
chat= model.start_chat(history=[])
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response
st.header("Gemini LLM Application")

# History
if 'chat_hstory' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input",key="input")
submit=st.button("Tell me the answer")

if submit and input:
    response=get_gemini_response(input)
    ##Add user query and response to session chat history
    st.session_state['chat_history'].append(("you",input))
    st.subheader("The responses is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("gemini", chunk.text))
st.subheader("The chat history is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
