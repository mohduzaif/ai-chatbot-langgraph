# import the required libraries.
import streamlit as st

from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage

# set the configuration variable.
CONFIG = {
    'configurable' : {
        'thread_id' : 'chat-1'
    }
}

# add the title on the top of the chat
st.markdown(
    """
    <h2 style="
        margin-top: 5px;
        margin-bottom: 10px;
        font-size: 20px;
    ">
        🤖 AI Assistant
    </h2>
    """,
    unsafe_allow_html=True
)


# create the list of messages so that messages can visible.
# st.session_state -> dict.
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# load the previous converstion from the history.
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# take the input from the user.
user_input = st.chat_input('Type here')

# check if user enter anything or not.
if user_input:

    # append the current input into a history.
    st.session_state['message_history'].append({'role' : 'user', 'content' : user_input})

    # print the current message to UI.
    with st.chat_message('user'):
        st.text(user_input)


    # called the llm for the query.
    response = chatbot.invoke({
        'messages' : HumanMessage(content = user_input)
    }, config = CONFIG)

    # extract the ai_message from the response comes from LLM.
    ai_message = response['messages'][-1].content

    # append the current input into a history.
    st.session_state['message_history'].append({'role' : 'assistant', 'content' : ai_message})
    
    # print the current message to UI.
    with st.chat_message('assistant'):
        st.text(ai_message)
