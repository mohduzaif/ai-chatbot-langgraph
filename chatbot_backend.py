
# import the required libraries.
from langgraph.graph import StateGraph, START, END
from langchain_cohere import ChatCohere
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver 

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

# define the checkpointer object.
checkPointer = InMemorySaver()


# define the graph.
graph = StateGraph(ChatState)

# add the nodes in the graph.
graph.add_node('chat_node', chat_node)

# add the edges in the graph.
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

# compile the graph.
chatbot = graph.compile(checkpointer = checkPointer)
