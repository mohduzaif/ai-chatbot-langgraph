# import the required libraries.
import streamlit as st

from streaming import stream_chat

from ui_sidebar.style import load_style
from ui_sidebar.sidebar import render_sidebar

from utils.thread import create_thread_id
from utils.add_thread import add_thread_id

from database.get_unique_thread_ids import get_all_unique_threads

# =========================
#    SESSION SETUP SECTION
# ========================= 
# create the list of messages so that messages can visible.
# st.session_state -> dict.
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# create the dictionary using the session_state.
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = create_thread_id()

# store the thread ids of the newly created chats.
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = get_all_unique_threads()

# add current thread_id.
add_thread_id(st.session_state['thread_id'])


# load the previous converstion from the history.
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# =========================
#    SIDEBAR
# ========================= 
# load the styling.
load_style()
# redner the sidebar
render_sidebar(st.session_state['thread_id'])


# =========================
#    CHAT UI SECTION
# ========================= 
# take the input from the user.
user_input = st.chat_input('Type here')

# check if user enter anything or not.
if user_input:

    # append the current input into a history.
    st.session_state['message_history'].append({'role' : 'user', 'content' : user_input})

    # print the current message to UI.
    with st.chat_message('user'):
        st.text(user_input)

    # looping ths stream object(generator) to get out the data
    # display the stream data using write_stream
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            stream_chat(user_input, st.session_state['thread_id'])
        )

    st.session_state['message_history'].append({'role' : 'assistant', 'content' : ai_message})