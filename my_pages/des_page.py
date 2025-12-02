import streamlit as st
from pyDes import des, ECB, PAD_PKCS5

def des_encrypt(text, key):
    cipher = des(key, ECB, padmode=PAD_PKCS5)
    return cipher.encrypt(text).hex()

def des_decrypt(hex_text, key):
    cipher = des(key, ECB, padmode=PAD_PKCS5)
    return cipher.decrypt(bytes.fromhex(hex_text)).decode()

def show_des_page():
    st.title("DES Cipher")

    st.subheader("Encryption")
    txt = st.text_input("Plaintext", key="des_plain")
    key = st.text_input("Key (8 chars)", key="des_key1")
    if st.button("Encrypt", key="des_enc_btn"):
        st.success(des_encrypt(txt, key))

    st.subheader("Decryption")
    txt2 = st.text_input("Ciphertext (HEX)", key="des_cipher")
    key2 = st.text_input("Key", key="des_key2")
    if st.button("Decrypt", key="des_dec_btn"):
        st.success(des_decrypt(txt2, key2))
