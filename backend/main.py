from fastapi import FastAPI
from backend.routers import food

app = FastAPI()
app.include_router(food.router)

