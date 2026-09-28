from langchain_core.messages import HumanMessage
from chatbot_backend import chatbot

# set the configuration variable.
CONFIG = {
    'configurable' : {
        'thread_id' : 'chat-1'
    }
}

def stream_chat(user_input):

    stream_data_object = chatbot.stream(
        {
            "messages": HumanMessage(content=user_input)
        },
        stream_mode="messages",
        config=CONFIG
    )

    for message_chunk, metadata in stream_data_object:
        yield message_chunk