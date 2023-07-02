from fastapi import FastAPI
from app.routers import infos

app = FastAPI()

app.include_router(infos.router)
