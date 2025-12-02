import streamlit as st

def affine_encrypt(p, a, b):
    return ''.join(chr(((a * (ord(ch) - 97) + b) % 26) + 97) for ch in p.lower() if ch.isalpha())

def affine_decrypt(c, a, b):
    # modular inverse of a mod 26
    for x in range(26):
        if (a * x) % 26 == 1:
            inv = x
            break
    return ''.join(chr(((inv * (ord(ch) - 97 - b)) % 26) + 97) for ch in c.lower() if ch.isalpha())

def show_affine_page():
    st.title("Affine Cipher")

    st.subheader("Encryption")
    text = st.text_input("Plaintext", key="affine_plain")
    a = st.number_input("Key a", min_value=1, max_value=25, step=1)
    b = st.number_input("Key b", min_value=0, max_value=25, step=1)

    if st.button("Encrypt", key="affine_enc_btn"):
        result = affine_encrypt(text, a, b)
        st.success(result)

    st.subheader("Decryption")
    text2 = st.text_input("Ciphertext", key="affine_ciph")
    a2 = st.number_input("Key a (again)", min_value=1, max_value=25, step=1)
    b2 = st.number_input("Key b (again)", min_value=0, max_value=25, step=1)

    if st.button("Decrypt", key="affine_dec_btn"):
        result2 = affine_decrypt(text2, a2, b2)
        st.success(result2)
