from fastapi import FastAPI

from src.app.endpoints.score_endpoints import score_router
from src.app.endpoints.user_endpoints import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(score_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
