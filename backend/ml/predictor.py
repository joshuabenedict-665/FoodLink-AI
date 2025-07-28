def match_surplus_to_needy(food_type, quantity, location):
    return {
        "suggested_organization": "Local Shelter A",
        "distance_km": 2.4,
        "urgency_level": "High"
    }
def classify_food(data: dict) -> str:
    # Dummy logic (can be replaced with actual model)
    if data["hours_since_prepared"] < 4 and data["temperature"] < 35:
        return "Safe"
    return "Unsafe"
