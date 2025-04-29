import streamlit as st
from cryptography.fernet import Fernet
from utlis import get_cipher, save_to_json
import hashlib
def insert_page():
    st.title("🔐 Insert New Data")
    with st.form("insert_form"):
        st.markdown("### Enter your Sensitive Data")

        data_name = st.text_input("Data Name*", help="Give a unique name to your Data")
        secret_text = st.text_area("Secret Text*", height=150, placeholder="Enter your confidential information here...")
        passkey = st.text_input("Create Passkey*", type="password", help="Strong passkey required for decryption") 
        confirm_passkey = st.text_input("Confirm Passkey*", type="password")

        # Form Submission
        submitted = st.form_submit_button("🔒 Encrypt & Store", type="primary")

        if submitted:
            if not all([data_name, secret_text,passkey, confirm_passkey]):
                st.error("Please fill all required fields!")
                return
            
            if passkey != confirm_passkey:
                st.error("Passkeys don't match!")
                return
            
            # Encryption Process
            cipher = get_cipher()
            hashed_pass = hashlib.sha256(passkey.encode()).hexdigest()
            encrypted_text = cipher.encrypt(secret_text.encode()).decode()

            # Store Data
            st.session_state.stored_data[data_name] = {
                "encrypted_text":encrypted_text,
                "passkey" : hashed_pass
            }

            save_to_json(st.session_state.stored_data)
            st.success("Data Encrypted and stored Successfully")
            st.balloons()
            st.session_state.current_page = "home"
            st.rerun()

    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()
