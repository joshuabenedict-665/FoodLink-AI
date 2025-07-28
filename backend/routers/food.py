from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.ml import predictor

router = APIRouter(prefix="/food", tags=["Food"])

class SurplusFood(BaseModel):
    food_type: str
    quantity: float
    location: str
    hours_since_prepared: int
    temperature: float

@router.post("/submit")
async def submit_surplus(data: SurplusFood):
    async def submit_surplus(data: SurplusFood):
    classification = predictor.classify_food(data.dict())
    
    if classification == "Unsafe":
        raise HTTPException(status_code=400, detail="Food is unsafe for donation.")

    match_result = predictor.match_surplus_to_needy(data.food_type, data.quantity, data.location)

    return {
        "message": "Food is safe and matched to an organization!",
        "data": match_result
    }
