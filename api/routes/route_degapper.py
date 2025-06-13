from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["mcp_public"])
def degapper():
    pass