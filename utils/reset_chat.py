from utils.thread import create_thread_id
from utils.add_thread import add_thread_id

import streamlit as st


def reset_ui():

    # generate new thread id.
    thread_id = create_thread_id()

    # Store the new thread ID.
    st.session_state['thread_id'] = thread_id

    #add the current thread_id into a chat_threads.
    add_thread_id(thread_id)

    # reset the ui.
    st.session_state['message_history'] = []

    # rerun the application.
    st.rerun()