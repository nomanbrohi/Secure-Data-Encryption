import streamlit as st
from insert import insert_page
from retrieve import retrieve_page
from login import login_page
from background import set_bg_hack

st.set_page_config(
    page_title="Secure Vault",
    page_icon="🛡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#session state initialization 
if 'current_page' not in st.session_state:
    st.session_state.current_page = "login"
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

#Home Page

def home_page():
    set_bg_hack()
    st.markdown("<h1 style='color:white; text-align:center;'>🔐 Secure Data Vault</h1>", unsafe_allow_html=True)

    # CSS for the whole columns block
    st.markdown("""
    <style>
        div[data-testid="stHorizontalBlock"]{
            background-color: rgba(165, 105, 189, 0.9); /* Purple Transparent Box */
            padding: 30px;
            border-radius: 15px;
            width: 600px;
            height:400px;
            margin: 20px auto;
            box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.2);
            text-align: center;
            display:flex;
            align-items:center;
            justify-content:center;
        }
        .stButton button {
            background-color: #6a0dad;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            margin: 10px 0px;
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Container with custom style
    with st.container():
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        # Trick: add an empty markdown with a special class to create a box

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("➕ Insert Data", use_container_width=True):
                st.session_state.current_page = "insert"
                st.rerun()
        with col2:
            if st.button("🔍 Retrieve Data", use_container_width=True):
                st.session_state.current_page = "retrieve"
                st.rerun()
        with col3:
            if st.button("👤 Login", use_container_width=True):
                st.session_state.current_page = "login"
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.current_page == "login":
    login_page()
elif st.session_state.current_page == 'insert':
    insert_page()
elif st.session_state.current_page == 'retrieve':
    retrieve_page()
elif st.session_state.current_page == 'home':
    home_page()
