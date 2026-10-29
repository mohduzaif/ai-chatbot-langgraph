
from dotenv import load_dotenv
import os

# Load the current .env values, replacing stale environment values.
load_dotenv(override=True)

print(
    "API key present:",
    bool(os.getenv("TAVILY_API_KEY"))
)

from langchain_tavily import TavilySearch

search = TavilySearch(max_results=2)

try:
    result = search.invoke({
        "query": "Who is the current CEO of Snap Inc.?"
    })
    print(result)
except Exception as exc:
    print(f"Search failed: {type(exc).__name__}: {exc}")
