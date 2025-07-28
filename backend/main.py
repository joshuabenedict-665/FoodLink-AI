from fastapi import FastAPI
from routers import food

app = FastAPI()
app.include_router(food.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Food Surplus API!"}
