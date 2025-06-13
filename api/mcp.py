from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import os

# FastAPI routes
from .routes import route_degapper
from .routes import route_general

app = FastAPI()

app.include_router(route_general.router)
app.include_router(route_degapper.router, prefix="/degapper", tags=["degapper"])

#mcp server
mcp = FastApiMCP(
    app,
    # Publish the endpoints having the tag "mcp_public" to the MCP server
    include_tags=["mcp_public"]
)
mcp.mount()

if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="127.0.0.1", port=8000)
    # For enabling hot reload
    filename = os.path.basename(__file__).replace('.py', '')
    uvicorn.run(f"{filename}:app", host="127.0.0.1", port=8000, reload=True)