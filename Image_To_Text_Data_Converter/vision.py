#Loading all the environment variables
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#Function to load gemini pro model andget responses
model = genai.GenerativeModel("gemini-pro-vision")
def get_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)    
    return response.text

## initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Image Application")
input=st.text_input("Input: ",key="input")
## upload file
uploaded_file = st.file_uploader("choose an image..", type=["jpg", "jpeg", "png",])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit  = st.button("Tell me about image")

## if submit is clicked
if submit:
    response = get_response(input,image)
    st.subheader("The Response is")
    st.write(response)
