"""xawpbe module."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware

from routes.hbeat import hbeat_router
from routes.login import login_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("initializing resources ...")
    yield
    print("destroying resources ...")

app = FastAPI(lifespan=lifespan)

print("starting server ...")

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(hbeat_router)
app.include_router(login_router)
