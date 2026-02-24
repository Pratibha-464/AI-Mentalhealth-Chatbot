import streamlit as st
from api import create_chat, send_message, generate_summary
from auth import init_auth, login_page, signup_page, guest_login, logout
from prompt import system_prompt


st.set_page_config(page_title='Mental Health Support 💚')

st.markdown("""
    <style>
    /* 1. Pull the entire sidebar content to the very top */
    [data-testid="stSidebarContent"] {
        padding-top: 0rem !important;
    }

    /* 2. Target the specific Logout Icon size */
    /* This makes the Material Icon significantly larger */
    [data-testid="stSidebar"] button[kind="tertiary"] i {
        font-size: 32px !important;
        width: 32px !important;
        height: 500px !important;
    }

    /* 3. Ensure the columns don't add extra padding */
    [data-testid="column"] {
        display: flex;
        align-items: start;
        justify-content: flex-start;
    }
    
    /* 4. Optional: Make the icon turn red on hover */
    [data-testid="stSidebar"] button[kind="tertiary"]:hover i {
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

init_auth()

if "chat_apps" not in st.session_state:
    st.session_state.chat_apps = {}

# For chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {}

# For Chat Summary
if 'chat_summary' not in st.session_state:
  st.session_state.chat_summary = {}

if "old_history" not in st.session_state: 
    st.session_state.old_history = {}

if "processing" not in st.session_state: 
    st.session_state.processing = False

if "chat_started" not in st.session_state:
    st.session_state.chat_started = False


if not st.session_state.logged_in:
   st.set_page_config(layout='centered')

   st.markdown("""
        <style>
        .page-header {
            text-align: center;
            color: #2d6a4f;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .page-subtitle {
            text-align: center;
            color: #52796f;
            font-size: 16px;
            margin-bottom: 25px;
        }
        </style>
    """, unsafe_allow_html=True)

   st.markdown('<div class="page-header">💚 Mental Health Support</div>', unsafe_allow_html=True)
   st.markdown('<div class="page-subtitle">Your safe place where you can share your thoughts.</div>', unsafe_allow_html=True)

   left, center, right = st.columns([0.5, 5, 0.5])

   with center:
       st.button('Continue as Guest', use_container_width=True, on_click=guest_login)
       st.divider()
       method = st.radio('Select:', ['Welcome Back', 'Create Account'], horizontal=True)
       if method == 'Welcome Back':
           login_page()
       else:
           signup_page()
   st.stop()

user = st.session_state.current_user

with st.sidebar:
    # 1. Create two columns: one for the small icon, one for the user text
    # The [1, 4] ratio makes the first column small for the icon
    col1, col2 = st.columns([1, 5])
    
    with col1:
        if st.button("", icon=":material/logout:", help="Logout", type="tertiary"):
            logout()
            
    with col2:
        st.markdown(f"""
            <div style='
                font-size: 24px; 
                font-weight: 500; 
                line-height: 1; 
                margin-left: -20px;
                margin-top: 5px;'>   
                {user}
            </div>
            """, unsafe_allow_html=True)

    st.markdown('----')

    # 2. MIDDLE: Summary
    st.subheader("🧠 Conversation Summary")
    if st.session_state.chat_summary.get(user):
        st.write(st.session_state.chat_summary[user])
    else:
        st.caption("No conversation yet...")



if user not in st.session_state.chat_apps:
    st.session_state.chat_apps[user] = create_chat(system_prompt)
if user not in st.session_state.chat_history:
    st.session_state.chat_history[user] = []
if user not in st.session_state.chat_summary:
    st.session_state.chat_summary[user] = ''
if user not in st.session_state.old_history:
    st.session_state.old_history[user] = []

chat_app = st.session_state.chat_apps[user]

if not st.session_state.chat_history[user]:
    st.title('💚 Mental Health Support Chatbot')
    st.write(
        "Hello! I’m your AI mental health assistant. "
        'You can talk about your feelings, ask questions, or just chat casually.'
    )

thinking_placeholder = st.empty()

user_input = st.chat_input('Enter your message.....', disabled = st.session_state.processing)

if user_input and not st.session_state.processing:
    st.session_state.chat_started = True
    st.session_state.processing = True

    st.session_state.chat_history[user].append(('user', user_input))
    
    thinking_placeholder.markdown('<i>Assistant is typing....</i>', unsafe_allow_html = True)
    
    reply = send_message(chat_app, user_input)
    st.session_state.chat_history[user].append(('assistant', reply))

    thinking_placeholder.empty() 
    st.session_state.processing = False  

    history = st.session_state.chat_history[user]
    if len(history) >= 6:
        new_msg = history[len(st.session_state.old_history[user]):-3]

        if new_msg:
            sum = generate_summary(chat_app, new_msg, exist=st.session_state.chat_summary[user])
            st.session_state.chat_summary[user] = sum
            st.session_state.old_history[user].extend(new_msg)       

chat_container = st.container()

with chat_container:
    for role, msg in st.session_state.chat_history[user]:

        if role == "user":
            col1, col2 = st.columns([1, 4])  
            with col2:
                st.markdown(
                    f"""
                    <div style="
                        display:inline-block;
                        background:#cce5ff;
                        padding:10px 14px;
                        border-radius:16px 16px 4px 16px;
                        max-width:75%;
                        margin-bottom:6px;
                        word-wrap:break-word;
                        text-align:left;
                        float:right;
                        clear:both;">
                        {msg}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:
            col1, col2 = st.columns([4, 1])  
            with col1:
                st.markdown(
                    f"""
                    <div style="
                        display:inline-block;
                        background:#d4edda;
                        padding:10px 14px;
                        border-radius:16px 16px 16px 4px;
                        max-width:75%;
                        margin-bottom:6px;
                        word-wrap:break-word;
                        text-align:left;">
                        {msg}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    
