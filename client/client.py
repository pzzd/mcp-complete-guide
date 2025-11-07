'''
run with
uv run client.py
'''

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

# server_params = StdioServerParameters(
#     command="uv",
#     args=["run", "weather.py"]
# )

server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
)

async def run():
    try:
        print ('starting')
        async with stdio_client(server_params) as (read, write):
            print ('client connected')
            async with ClientSession(read, write) as session:
                print ('init session')
                await session.initialize()

                print('listening tools')
                tools = await session.list_tools()
                print ('available tools ', tools)

                print ('calling tool')
                # LLM would determine location value
                # result = await session.call_tool("get_weather", arguments={"location": "California"} )
                result = await session.call_tool("airbnb_search", arguments={"location": "California"} )

                print ('tool result ', result)
                
    except Exception as e:
        print('an error')
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())