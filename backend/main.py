from fastapi import FastAPI
from routers import food

app = FastAPI(
    title="FoodLink AI",
    description="An AI-powered platform to reduce urban food waste",
    version="1.0.0"
)
app.include_router(food.router)
