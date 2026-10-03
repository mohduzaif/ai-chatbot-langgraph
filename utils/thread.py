
# import the required Library.
import uuid

# create the function that is used to create the new thread id.
def create_thread_id():

    # generate the thread_id.
    thread_id = uuid.uuid4()
    
    # return the thread_id
    return thread_id