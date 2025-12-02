import streamlit as st
from my_pages.affine_page import show_affine_page
from my_pages.dna_page import show_dna_page
from my_pages.vigenere_page import show_vigenere_page
from my_pages.row_page import show_row_page
from my_pages.des_page import show_des_page
from my_pages.aes_page import show_aes_page
from my_pages.history_page import show_history_page

st.set_page_config(page_title="Crypto App", layout="wide")

with st.sidebar:
    st.title("🔐 Algorithms")
    page = st.radio(
        "Navigate to:",
        ["Dashboard", "Affine", "DNA", "Vigenère", "Row Transposition", "DES", "AES", "History"],
        key="menu"
    )

if page == "Dashboard":
    st.title("Welcome to Crypto App")
    st.write("Choose an algorithm from the sidebar to begin.")

elif page == "Affine":
    show_affine_page()

elif page == "DNA":
    show_dna_page()

elif page == "Vigenère":
    show_vigenere_page()

elif page == "Row Transposition":
    show_row_page()

elif page == "DES":
    show_des_page()

elif page == "AES":
    show_aes_page()

elif page == "History":
    show_history_page()
