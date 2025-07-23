from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/food", tags=["Food"])

class SurplusFood(BaseModel):
    food_type: str
    quantity: float
    location: str

@router.post("/submit")
async def submit_surplus(data: SurplusFood):
    return {
        "message": "Surplus food data received!",
        "data": data
    }
