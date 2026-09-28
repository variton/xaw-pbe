"hbeat module."

from fastapi import APIRouter


hbeat_router = APIRouter(prefix="/api/hbeat", tags=["hbeat"])

@hbeat_router.get("/")
async def hbeat():
    return {"hbeat": "ok"}


