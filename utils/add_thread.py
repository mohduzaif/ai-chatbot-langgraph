
import streamlit as st 

def add_thread_id(thread_id): 

    # check whether the given thread_id not present in session_thread.
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)