from langchain_core.messages import HumanMessage
from chatbot_backend import chatbot

def stream_chat(user_input, thread_id):

    # =========================
    #    SET CONFIGURATION VARIABLE.
    # ========================= 
    CONFIG = {
        'configurable' : {
            'thread_id' : thread_id
        }
    }
    stream_data_object = chatbot.stream(
        {
            "messages": HumanMessage(content=user_input)
        },
        stream_mode="messages",
        config=CONFIG
    )

    for message_chunk, metadata in stream_data_object:
        yield message_chunk