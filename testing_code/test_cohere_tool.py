
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_cohere import ChatCohere
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatCohere(
    model="command-a-03-2025",
    temperature=0
)

search_tool = TavilySearch(max_results=2)
model_with_tools = model.bind_tools([search_tool])

messages = [
    SystemMessage(
        content=(
            "You are an assistant with a web search tool. "
            "For questions about current facts, call the search "
            "tool with a meaningful, non-empty query. "
            "Do not invent tool names or arguments."
        )
    ),
    HumanMessage(
        content="Who is the current CEO of Snap Inc.?"
    ),
]

response = model_with_tools.invoke(messages)

print("\n--- Response content ---")
print(response.content)

print("\n--- Valid tool calls ---")
print(response.tool_calls)

print("\n--- Invalid tool calls ---")
print(response.invalid_tool_calls)

print("\n--- Raw response metadata ---")
print(response.response_metadata)
