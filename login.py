import streamlit as st
import base64
from PIL import Image

def set_bg_hack(image_path="bg.jpg"):
    try:
        Image.open(image_path)
        with open(image_path, "rb") as f:
            img_bytes = f.read()
        encoded = base64.b64encode(img_bytes).decode()

        st.markdown(
            f"""
            <style>
            [data-testid="stAppViewContainer"] {{
                background: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            [data-testid="stForm"] {{
                background-color: rgba(255, 255, 255, 0.85);
                padding: 2rem;
                border-radius: 15px;
                width: 800px;
                margin: 100px auto; /* Center the form */
                box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.2);
            }}

            h1.text-color{{
                color: white;
                text-align: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Background image error: {str(e)}")


def login_page():
    set_bg_hack()

    st.markdown("<h1 class='text-color'>👤 Login</h1>", unsafe_allow_html=True)
    # st.title("Login")
    # Simple Form
    with st.form("login_form"):
        username = st.text_input("Username", help="admin")
        password = st.text_input("Password", type="password", help="secure123")
        
        submit = st.form_submit_button("Login")
        
        if submit:
            if username == "admin" and password == "secure123":
                st.success("✅ Login successful!")
                st.session_state.login_status = True
                st.session_state.current_page = "home"
                st.rerun()
            else:
                st.error("❌ Invalid credentials!")
