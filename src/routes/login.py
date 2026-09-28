"""login module."""


from fastapi import APIRouter, HTTPException, status, Request
from fastapi import Response
from pydantic import BaseModel


class LoginCredentials(BaseModel):
    """Credentials supplied in the login request body."""

    email: str
    pwd: str

login_router = APIRouter(prefix="/api/login", tags=["login"])

@login_router.post("/",
                  status_code=status.HTTP_200_OK,
                  response_model=dict)
async def login(credentials: LoginCredentials,request:Request,response:Response):
    if credentials.email == "morpheus@matrix.com" and credentials.pwd == "1234":
        token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxx"

        response.set_cookie(key="access_token",
                            value=token,
                            httponly=True,
                            secure=False,    # Local HTTP development only; use True with HTTPS
                            samesite="lax",
                            path="/")
        return {"ok":True}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
