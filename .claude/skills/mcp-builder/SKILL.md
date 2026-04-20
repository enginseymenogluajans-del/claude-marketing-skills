---
name: mcp-builder
description: Use when the user asks to create, build, or set up an MCP server, integrate an external API via MCP, or build a Model Context Protocol server. Supports Python (FastMCP) and TypeScript SDK. Trigger keywords: MCP server, MCP, Model Context Protocol, FastMCP, MCP tool, MCP integration, create MCP.
---

# MCP Builder

## Overview
Create MCP (Model Context Protocol) servers that integrate external APIs as tools Claude can use. Supports Python (FastMCP) and TypeScript SDK.

## Steps

1. Ask: which API to integrate? What tools/resources to expose?
2. Choose language: Python (simpler) or TypeScript (more control)
3. Scaffold the server
4. Register in Claude Code settings

## Python — FastMCP

```python
# Install: pip install fastmcp httpx
from fastmcp import FastMCP

mcp = FastMCP("my-api-server")

@mcp.tool()
async def search_items(query: str, limit: int = 10) -> list[dict]:
    """Search for items matching query."""
    import httpx
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://api.example.com/search",
            params={"q": query, "limit": limit},
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        return resp.json()["results"]

@mcp.resource("items://{item_id}")
async def get_item(item_id: str) -> str:
    """Get item details."""
    import httpx
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://api.example.com/items/{item_id}")
        return resp.text

if __name__ == "__main__":
    mcp.run()
```

## TypeScript — MCP SDK

```typescript
// Install: npm install @modelcontextprotocol/sdk
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({ name: "my-server", version: "1.0.0" }, {
  capabilities: { tools: {} }
});

server.setRequestHandler("tools/list", async () => ({
  tools: [{
    name: "search",
    description: "Search items",
    inputSchema: {
      type: "object",
      properties: { query: { type: "string" } },
      required: ["query"]
    }
  }]
}));

server.setRequestHandler("tools/call", async (request) => {
  const { name, arguments: args } = request.params;
  if (name === "search") {
    const result = await fetch(`https://api.example.com/search?q=${args.query}`);
    return { content: [{ type: "text", text: await result.text() }] };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Register in Claude Code
Add to `.claude/settings.json`:
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": [".claude/mcp_servers/my_server.py"],
      "env": { "API_KEY": "your-key" }
    }
  }
}
```

## Output Format
- Create server file at `.claude/mcp_servers/<name>.py` or `.ts`
- Update settings.json with server registration
- List exposed tools and their parameters
