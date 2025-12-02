import streamlit as st

def show_history_page():
    st.title("History")

    if "history" not in st.session_state:
        st.session_state["history"] = []

    st.write("### Previous Encryption/Decryption")

    for item in st.session_state["history"]:
        st.info(f"**{item['algo']}** → {item['action']} \n\nInput: `{item['input']}` \nResult: `{item['output']}`")
