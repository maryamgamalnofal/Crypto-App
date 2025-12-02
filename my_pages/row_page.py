import streamlit as st

# ---------------- Row Transposition Encryption ---------------- #
def row_encrypt(msg, key):
    msg = msg.replace(" ", "")
    key_order = sorted(list(key))

    # إنشاء أعمدة لكل حرف في المفتاح
    columns = {k: "" for k in key_order}

    # التوزيع على الأعمدة
    for i, ch in enumerate(msg):
        col_key = key_order[i % len(key)]
        columns[col_key] += ch

    # قراءة النص بالأعمدة المرتبة
    return ''.join(columns[k] for k in key_order)


# ---------------- Row Transposition Decryption ---------------- #
def row_decrypt(cipher, key):
    cipher = cipher.replace(" ", "")
    key_order = sorted(list(key))
    col_length = len(cipher) // len(key)

    # فصل النص المشفر إلى أعمدة
    cols = {}
    idx = 0
    for k in key_order:
        cols[k] = cipher[idx:idx + col_length]
        idx += col_length

    # إعادة تجميع النص من الأعمدة
    result = ""
    for i in range(col_length):
        for k in key:
            result += cols[k][i]
    return result


# ---------------- Streamlit Page ---------------- #
def show_row_page():
    st.title("Row Transposition Cipher")

    st.subheader("Encryption")
    msg = st.text_input("Plaintext", key="row_plain")
    key = st.text_input("Key", key="row_key1")

    if st.button("Encrypt", key="row_enc_btn"):
        if key == "":
            st.error("Key cannot be empty.")
        else:
            st.success(row_encrypt(msg, key))

    st.subheader("Decryption")
    msg2 = st.text_input("Ciphertext", key="row_cipher")
    key2 = st.text_input("Key", key="row_key2")

    if st.button("Decrypt", key="row_dec_btn"):
        if key2 == "":
            st.error("Key cannot be empty.")
        else:
            st.success(row_decrypt(msg2, key2))
