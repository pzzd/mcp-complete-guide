from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image
import pyautogui
import io


mcp = FastMCP("Screenshot Demo")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Capture the current screen and return the image. Use this tool whenver the user requests
    """

    buffer = io.BytesIO()

    # claude will reject if >1MB
    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
    return Image(data=buffer.getValue(), format="jpeg")

if __name__ == "__main__":
    mcp.run()