import streamlit as st
from model import get_response
from translate import traduzir_texto_para_en, traduzir_texto_para_pt

st.title("Blender Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    
    promptEn = traduzir_texto_para_en(prompt)
    
    response = get_response(promptEn)
    
    responsePt = traduzir_texto_para_pt(response)
    
    with st.chat_message("assistant"):
        st.markdown(responsePt)
    st.session_state.messages.append({"role": "assistant", "content": responsePt})