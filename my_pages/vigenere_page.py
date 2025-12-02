import streamlit as st

def format_text(s):
    return ''.join([c.upper() for c in s if c.isalpha()])

def vigenere_encrypt(p, key):
    p = format_text(p)
    key = format_text(key)
    res = ""
    for i, ch in enumerate(p):
        shift = ord(key[i % len(key)]) - 65
        res += chr((ord(ch) - 65 + shift) % 26 + 65)
    return res

def vigenere_decrypt(c, key):
    c = format_text(c)
    key = format_text(key)
    res = ""
    for i, ch in enumerate(c):
        shift = ord(key[i % len(key)]) - 65
        res += chr((ord(ch) - 65 - shift) % 26 + 65)
    return res

def show_vigenere_page():
    st.title("Vigenère Cipher")

    st.subheader("Encryption")
    text = st.text_input("Plaintext", key="vig_plain")
    key = st.text_input("Key", key="vig_key1")
    if st.button("Encrypt", key="vig_enc_btn"):
        st.success(vigenere_encrypt(text, key))

    st.subheader("Decryption")
    text2 = st.text_input("Ciphertext", key="vig_cipher")
    key2 = st.text_input("Key", key="vig_key2")
    if st.button("Decrypt", key="vig_dec_btn"):
        st.success(vigenere_decrypt(text2, key2))
