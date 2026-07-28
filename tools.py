import uuid
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import tool
from datetime import datetime 

duckduckgo = DuckDuckGoSearchRun()
@tool
def search_tool(query: str) -> str:
    """Search the internet for current information."""

    return duckduckgo.run(query)

api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=1000,
)

wiki_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper
)