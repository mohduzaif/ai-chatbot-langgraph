
# import the required libraries.
from langgraph.graph import StateGraph, START, END
from langchain_cohere import ChatCohere
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver 
from database.sqlite_db import get_database_connection_obj

# load the environment variables.
load_dotenv()

# create the model object.
model = ChatCohere(
    model = 'command-a-03-2025', 
    temperature = 0.7
)

# define the state.
class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]


# define the node.

# define the chat_node.
def chat_node(state : ChatState):

    # fetch the message for query.
    messages = state['messages']

    # invoke the function.
    response = model.invoke(messages)

    # update the state.
    return {
        'messages' : [response]
    }

# get the db connection object.
conn = get_database_connection_obj() 

# define the checkpointer object.
checkPointer = SqliteSaver(conn = conn)


# define the graph.
graph = StateGraph(ChatState)

# add the nodes in the graph.
graph.add_node('chat_node', chat_node)

# add the edges in the graph.
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

# compile the graph.
chatbot = graph.compile(checkpointer = checkPointer)