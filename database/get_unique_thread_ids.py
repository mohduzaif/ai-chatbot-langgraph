
# Import Required Libraries.
from chatbot_backend import checkPointer

# function to get all unique_ids from database.
def get_all_unique_threads():
    
    # create the set to collect unique thread_ids from the database.
    all_unique_thread = set()

    # collect all unique threads from the database.
    for checkpoint in checkPointer.list(None):
        all_unique_thread.add(checkpoint.config['configurable']['thread_id'])

    return list(all_unique_thread)