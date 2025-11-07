'''
decorator creates this info:

  meta=None nextCursor=None tools=[Tool(name='get_weather', title=None, description='Get the current weather for a given location.', inputSchema={'properties': {'location': {'title': 'Location', 'type': 'string'}}, 'required': ['location'], 'title': 'get_weatherArguments', 'type': 'object'}, outputSchema={'properties': {'result': {'title': 'Result', 'type': 'string'}}, 'required': ['result'], 'title': 'get_weatherOutput', 'type': 'object'}, icons=None, annotations=None, meta=None)]
'''
from mcp.server.fastmcp import FastMCP

# name here is significant
mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # In a real implementation, this function would call a weather API.
    # Here, we return a mock response for demonstration purposes.
    return f"The current weather in {location} is sunny with a temperature of 25°C."


if __name__ == "__main__":
    mcp.run()
    