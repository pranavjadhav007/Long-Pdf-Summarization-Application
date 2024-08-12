from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
GEN_API_KEY=os.getenv("Gemini_API_key")
import google.generativeai as genai

genai.configure(api_key=GEN_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
prompt="""
You are expert that generates summaries by selecting and combining the most important sentences from the provided document only. You are good in processing the large documents.
Concise Summary:''
Generate in above format only.
"""
st.title("Summary Generator")
doc=st.file_uploader("Upload the Document you want to process.",type=["pdf", "txt","docx"])
button_click=st.button("Process the document")
if button_click:
    with open("uploadedfile.pdf", "wb") as f:
        f.write(doc.getbuffer())
    sample_file = genai.upload_file(path="uploadedfile.pdf",display_name="mypdf")
    response = model.generate_content([sample_file,prompt])
    if response:
        st.write(response.text)
    else:
        st.write("File Upload extension Problem")
    os.remove("uploadedfile.pdf")



