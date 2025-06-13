from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["degapper", "mcp_public"])
def degapper():
    pass