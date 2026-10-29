
# Import the required Libraries.
from langchain_tavily import TavilySearch

# create the web search object.
web_search = TavilySearch(
    max_results=3,
    search_depth="basic",
    include_answer=True,
    include_raw_content=False,
    include_images=False,
)

