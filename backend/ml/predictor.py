import numpy as np
from keras.models import load_model
import pickle
import os
model_path=os.path.join("backend", "ml", "model", "food_safety_model.h5");
scaler_path=os.path.join("backend", "ml", "model", "scaler.pkl");
model=load_model(model_path)
with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)
def match_surplus_to_needy(food_type, quantity, location):
    return {
        "suggested_organization": "Local Shelter A",
        "distance_km": 2.4,
        "urgency_level": "High"
    }
def classify_food(data: dict) -> str:
    # Dummy logic (can be replaced with actual model)
    features = np.array([[data["quantity"], data["hours_since_prepared"], data["temperature"]]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0][0]
    return "Safe" if prediction > 0.5 else "Unsafe"
