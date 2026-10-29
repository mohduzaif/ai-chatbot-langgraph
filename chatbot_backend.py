
# import the required libraries.
from langgraph.graph import StateGraph, START, END
from langchain_cohere import ChatCohere
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, AIMessage, SystemMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver 
from database.sqlite_db import get_database_connection_obj

import os

# import tool related libaries.
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool

# load the environment variables.
load_dotenv(override = True)

# for debugging.
# print(
#     "Tavily API key loaded:",
#     bool(os.getenv("TAVILY_API_KEY"))
# )

# import all the tools.
# from tools.calculator_tool import calculator
# from tools.stock_tool import get_stock_price
from tools.web_search_tool import web_search

# create the model object.
model = ChatCohere(
    model = 'command-a-03-2025', 
    temperature = 0
)

# create the tool list.
tools = [web_search]

# create the LLM with having tools.
model_with_tool = model.bind_tools(tools)

# define the state.
class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]


# define the node.

# REQUIRED_ARGS = {
#     web_search.name: {"query"},
# }

SYSTEM_PROMPT = SystemMessage(
    content=f"""
    You are a helpful AI assistant.

    You have access to the following tool:
    - {web_search.name}(query): searches the web.

    For greetings and general conversation, answer normally.
    For current facts or questions requiring web research,
    call the web search tool with a meaningful, non-empty query.

    Use one search query that covers the user's question.
    Do not invent tool names or arguments.
    After receiving the search results, answer using the results
    and include relevant source URLs when available.
    """
)

# define the chat node.
def chat_node(state: ChatState):
    messages = state["messages"]

    # response = model_with_tool.invoke(
    #     [SYSTEM_PROMPT, *messages]
    # )

    
    # Stream the Cohere response and combine chunks into one message.
    response = None

    for chunk in model_with_tool.stream(
        [SYSTEM_PROMPT, *messages]
    ):
        if response is None:
            response = chunk
        else:
            response = response + chunk

    if response is None:
        return {
            "messages": [
                AIMessage(content="I couldn't generate a response.")
            ]
        }


    # Keep only valid Tavily calls with a non-empty query.
    valid_calls = []

    for call in response.tool_calls:
        name = call.get("name", "")
        args = call.get("args", {})

        if (
            name == web_search.name
            and isinstance(args, dict)
            and isinstance(args.get("query"), str)
            and args["query"].strip()
        ):
            valid_calls.append(call)

    # Execute valid search calls even if other calls are malformed.
    if valid_calls:
        response = response.model_copy(
            update={
                "tool_calls": valid_calls,
                "invalid_tool_calls": [],
            }
        )
        return {"messages": [response]}

    # A malformed tool request should not reach ToolNode.
    if response.invalid_tool_calls or response.tool_calls:
        print("No valid web search calls were generated.")

        return {
            "messages": [
                AIMessage(
                    content=(
                        "I couldn't prepare a valid web search request. "
                        "Please try asking your question again."
                    )
                )
            ]
        }

    # Ordinary questions, such as greetings, reach this branch.
    return {"messages": [response]}


tool_node = ToolNode(tools)

# get the db connection object.
conn = get_database_connection_obj() 

# define the checkpointer object.
checkPointer = SqliteSaver(conn = conn)


# define the graph.
graph = StateGraph(ChatState)

# add the nodes in the graph.
graph.add_node('chat_node', chat_node)
graph.add_node('tools', tool_node)

# add the edges in the graph.
graph.add_edge(START, 'chat_node')
graph.add_conditional_edges('chat_node', tools_condition)
graph.add_edge('tools', 'chat_node')

# compile the graph.
chatbot = graph.compile(checkpointer = checkPointer)