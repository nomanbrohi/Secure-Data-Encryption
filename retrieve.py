import streamlit as st
from utlis import get_cipher, load_from_json
import hashlib
import time


def retrieve_page():

    st.title("🔓 Retrieve Your Data")

    if not st.session_state.stored_data:
        st.session_state.stored_data = load_from_json()

    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'lock_time' not in st.session_state:
        st.session_state.lock_time = 0

    if st.session_state.lock_time > time.time():
        remaining = int(st.session_state.lock_time - time.time())
        st.error(f"🔒 Account locked! Please try again in {remaining} seconds")
        return
    
    # Main Form
    with st.form("retrieve_form"):
        data_name = st.selectbox(
            "Select Data Name",
            options=list(st.session_state.stored_data.keys()),
            help="Select which data you want to retrieve")
        
        passkey = st.text_input(
            "Enter Passkey*",
            type="password")
        
        submitted = st.form_submit_button("Decrypt Data", type= "primary")

        if submitted:
            if not passkey:
                st.error("Please Enter Your Passkey")
                st.rerun
            
            stored = st.session_state.stored_data[data_name]
            
            hashed_input = hashlib.sha256(passkey.encode()).hexdigest()
            if "passkey" in stored:
                if hashed_input == stored["passkey"]:
                    cipher = get_cipher()
                    decrypted = cipher.decrypt(stored["encrypted_text"].encode()).decode()

                    st.success("✅ Data decrypted successfully!")
                    st.text_area("Decrypted Content", 
                                value=decrypted,
                                height=200)
                    st.session_state.attempts = 0
                else:
                    st.session_state.attempts += 1
                    remaining = 3 - st.session_state.attempts

                    if st.session_state.attempts >= 3:
                        st.session_state.lock_time = time.time() + 10
                        st.error("🚨 Too many failed attempts! System locked for 10 seconds.")
                    else:
                        st.warning(f"❌ Incorrect passkey! {remaining} attempts remaining")
    
    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()
            
        