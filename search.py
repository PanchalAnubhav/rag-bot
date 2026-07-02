""" this module provides a simple function to perform web searches using the DuckDuckGo API. """
import requests

def search_web(query: str) -> str:
    resp = requests.get(
        "https://api.duckduckgo.com/",
        params={"q": query, "format": "json", "no_html": 1},
    )
    data = resp.json()
    return data.get("AbstractText", "") or "No summary available."