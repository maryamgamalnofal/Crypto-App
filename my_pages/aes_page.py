import streamlit as st
from Crypto.Cipher import AES
import base64

def pad(s):
    return s + (16 - len(s)%16) * chr(16 - len(s)%16)

def unpad(s):
    return s[:-ord(s[-1])]

def aes_encrypt(text, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(text).encode())).decode()

def aes_decrypt(enc, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(enc)).decode())

def show_aes_page():
    st.title("AES Cipher")

    st.subheader("Encryption")
    txt = st.text_input("Plaintext", key="aes_plain")
    key = st.text_input("Key (16 chars)", key="aes_key1")

    if st.button("Encrypt", key="aes_enc_btn"):
        st.success(aes_encrypt(txt, key))

    st.subheader("Decryption")
    txt2 = st.text_input("Ciphertext (Base64)", key="aes_cipher")
    key2 = st.text_input("Key", key="aes_key2")

    if st.button("Decrypt", key="aes_dec_btn"):
        st.success(aes_decrypt(txt2, key2))
