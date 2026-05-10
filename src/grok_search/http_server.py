from __future__ import annotations

import os

from grok_search.server import mcp


def main() -> None:
    host = os.environ.get("MCP_HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_PORT", "8000"))
    path = os.environ.get("MCP_PATH", "/mcp/")

    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path = path + "/"

    mcp.run(transport="http", host=host, port=port, path=path)


if __name__ == "__main__":
    main()
