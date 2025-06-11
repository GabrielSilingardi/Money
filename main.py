import streamlit as st
import yfinance as yf

st.set_page_config(
    layout="wide",
    page_icon="📈",
    page_title="Titulo"
)

ticker = yf.Ticker("MSFT34")

st.markdown("<h1 style='text-align: center;'>Título da Página</h1>", unsafe_allow_html=True)

st.write(ticker)