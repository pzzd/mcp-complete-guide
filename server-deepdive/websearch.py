from mcp.server.fastmcp import FastMCP
from openai import OpenAI

mcp = FastMCP("Web Search")

@mcp.tool()
def perform_websearch(query: str) -> str:
    """
    Performs a web search for a query
    Args:
        query: the query to web search
    """

    messages = [
        {
            "role": "system",
            "content": ( "You are an AI assistant that searches the web and responds to queries.")
        },
        {
            "role": "user",
            "content": (query)
        }
    ]

    # Perplexity uses same standard as OpenAI. Use the perplexity API key here.
    # I don't have an API key. This code isn't tested.
    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")
    
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    mcp.run()