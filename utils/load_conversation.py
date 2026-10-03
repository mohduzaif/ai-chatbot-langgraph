from chatbot_backend import chatbot

def load_current_thread_conversation(thread_id):

    # set the configuration with current thread id.
    CONFIG = {
            'configurable' : {
                'thread_id' : thread_id
            }
        }
    return chatbot.get_state(config = CONFIG).values['messages']