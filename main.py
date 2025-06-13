import os
from api.mcp import app


def main():
    import uvicorn
    #uvicorn.run(app, host="127.0.0.1", port=8000)
    # For enabling hot reload
    filename = os.path.basename(__file__).replace('.py', '')
    uvicorn.run(f"{filename}:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()