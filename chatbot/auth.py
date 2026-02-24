import streamlit as st
import time

def init_auth():
    if 'users' not in st.session_state: 
        st.session_state.users = {}

    if 'logged_in' not in st.session_state: 
        st.session_state.logged_in = False

    if 'current_user' not in st.session_state:
        st.session_state.current_user = None

def show_toast(message, type='success', duration=2):
    color = '#d4edda' if type=='success' else '#f8d7da' if type=='error' else '#cce5ff'
    st.markdown(
        f"""
        <div style="
            position: fixed;
            bottom: 50px;
            right: 20px;
            background:{color};
            padding:20px 50px;
            border-radius:8px;
            z-index:9999;
            box-shadow:0px 2px 6px rgba(0,0,0,0.2);
            font-weight:bold;
        ">
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(duration)

def signup_page():
    with st.form('signup_form', clear_on_submit=False):
        new_username = st.text_input('New Username')
        new_password = st.text_input('New Password', type='password')
        submit = st.form_submit_button('Sign Up', use_container_width=True)

        if submit:
            if not new_username or not new_password:
                show_toast('Please enter both username and password ❌', type = 'error')
            elif new_username in st.session_state.users:
                show_toast('Username already exists ❌', type = 'error')
            else:
                st.session_state.users[new_username] = new_password
                st.session_state.logged_in = True
                st.session_state.current_user = new_username
                show_toast('Account Created.Logging you in...!!✅', type = 'success')
                st.rerun()


def login_page():

    with st.form('login_form', clear_on_submit=False):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')

        submit = st.form_submit_button('Login', use_container_width=True)

        if submit:
            if not username or not password:
                show_toast('Please enter both username and password ❌', type = 'error')
            elif username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.session_state.current_user = username
                show_toast('Logging in Successful! ✅', type='success')
                st.rerun()
            else:
                show_toast('Invalid username or password ❌', type = 'error')


def guest_login():
    st.session_state.logged_in = True
    st.session_state.current_user = 'guest'
    show_toast('Logging in as Guest !!!✅', type = 'info')


def logout():
  st.session_state.logged_in = False
  st.session_state.current_user = None
  show_toast('Logged out Successful !!! ✅', type = 'success')
  st.rerun()
  
