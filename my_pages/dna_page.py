import streamlit as st

mapping = {"A":"T", "T":"A", "C":"G", "G":"C"}

def dna_encrypt(seq):
    return ''.join(mapping.get(ch.upper(), ch) for ch in seq)

def dna_decrypt(seq):
    return dna_encrypt(seq)  # reverse is same

def show_dna_page():
    st.title("DNA Cipher")

    st.subheader("Encryption")
    seq = st.text_input("DNA Sequence (A,T,C,G)", key="dna_plain")
    if st.button("Encrypt", key="dna_enc_btn"):
        st.success(dna_encrypt(seq))

    st.subheader("Decryption")
    seq2 = st.text_input("Cipher Sequence", key="dna_cipher")
    if st.button("Decrypt", key="dna_dec_btn"):
        st.success(dna_decrypt(seq2))
