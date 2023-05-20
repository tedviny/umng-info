from fastapi import FastAPI
from routers import infos

app = FastAPI()

app.include_router(infos.router)

@app.get("/")
async def read_root():
    return "App is working!!!"