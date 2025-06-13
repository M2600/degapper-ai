from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@router.get("/twice", tags=["mcp_public"])
def twice(num: int):
    """
    Returns the input number multiplied by two.
    """
    return {"result": num * 2}

@router.get("/keyword", tags=["mcp_public"])
def keyword_endpoint():
    """
    A simple endpoint to demonstrate functionality.
    """
    return {"message": "keyword is 'Hello github copilot'"}