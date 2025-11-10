''' 
To run local server:
    mcp dev local.py

To install in Claude desktop:
    mcp install local.py
'''

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalNotes")

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Appends the given content to the user's local notes
    Args:
        content: The text content to append
    """
    filename = '/Users/pezzutidyer/Projects/mcp-complete-guide/server-deepdive/notes.txt'

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return f"Content appended to {filename}"
    except Exception as e:
        return f"Error appending to file: {e}"

@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the contents of the user's local notes
    """
    filename = '/Users/pezzutidyer/Projects/mcp-complete-guide/server-deepdive/notes.txt'

    try: 
        with open(filename, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes if notes else "No notes found"
    except FileNotFoundError:
        return "No notes file found"
    except Exception as e:
        return f"Error reading: {e}"

if __name__ == "__main__":
    mcp.run()