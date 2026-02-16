import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="SPRING AI SHIFT", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    .stApp h1, .stApp h2, .stApp p, .stApp label, .stApp span { color: #FFFFFF !important; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 1px solid #333333; }
    .stButton>button {
        width: 100%;
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: bold !important;
    }
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: #1a1a1a !important;
        border: 1px solid #FFFFFF !important;
    }
    textarea, input { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("Configuración")
    api_key = st.text_input("Gemini API Key:", type="password")
    st.divider()
    rol = st.selectbox("Perfil del usuario:", ["Dueño de negocio", "Content Manager", "Estudiante"])

st.title("SPRING AI SHIFT™")
col1, col2 = st.columns(2)

with col1:
    st.write("### Consulta")
    user_input = st.text_area("Input", placeholder="Escribe aquí...", height=200, label_visibility="collapsed")
    enviar = st.button("GENERAR")

with col2:
    st.write("### Resultado")
    if enviar:
        if not api_key:
            st.error("Ingresa la API Key")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"Actúa como un mentor experto en marketing. El usuario es: {rol}. Responde a: {user_input}"
                
                response = model.generate_content(prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
