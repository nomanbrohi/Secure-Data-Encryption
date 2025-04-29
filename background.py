
# background.py
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

            [data-testid="stColumns"] {{
                background-color: rgba(165, 105, 189, 0.85); /* Purple color */
                padding: 2rem;
                border-radius: 15px;
                width: 800px;
                margin: 100px auto;
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
