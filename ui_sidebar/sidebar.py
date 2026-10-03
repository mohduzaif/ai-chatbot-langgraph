import streamlit as st

from langchain_core.messages import HumanMessage

from utils.reset_chat import reset_ui
from utils.load_conversation import load_current_thread_conversation


def render_sidebar(thread_id):

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-title">
                🤖 AI Assistant
            </div>
            """,
            unsafe_allow_html=True
        )


        # =========================
        # NEW CHAT
        # =========================

        if st.button(
            "New Chat",
            key="new_chat",
            type="primary"
        ):
            reset_ui()


        # =========================
        # MY CONVERSATION
        # =========================

        st.markdown(
            """
            <div class="conversation-box">
                💬 My Conversation
            </div>
            """,
            unsafe_allow_html=True
        )


        # =========================
        # CHAT THREADS
        # =========================

        for chat_thread_id in st.session_state['chat_threads'][::-1]:

            if st.button(chat_thread_id, key=f"thread_{chat_thread_id}", type="secondary"):

                st.session_state['thread_id'] = chat_thread_id 

                # load the chat of the current thread.
                messages = load_current_thread_conversation(chat_thread_id)

                # convert the chat_format in competable format.
                temp_messages = []

                for msg in messages:
                    if isinstance(msg, HumanMessage):
                        role = 'user'
                    else:
                        role = 'assistant'

                    temp_messages.append({
                        'role' : role, 
                        'content' : msg.content
                    })


                st.session_state['message_history'] = temp_messages
                st.rerun()