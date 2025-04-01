from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Allow frontend to access the backend API (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL for production, e.g. ["https://yourapp.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model pipeline
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define input schema using all raw features expected by the pipeline
class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: float
    stories: float
    mainroad: str           # "yes" or "no"
    guestroom: str          # "yes" or "no"
    basement: str           # "yes" or "no"
    hotwaterheating: str    # "yes" or "no"
    airconditioning: str    # "yes" or "no"
    parking: int
    prefarea: str           # "yes" or "no"
    furnishingstatus: str   # "furnished", "semi-furnished", "unfurnished"

@app.get("/")
def read_root():
    return {"message": "🏠 House Pricing Model is live!"}

@app.post("/predict")
def predict(data: HouseData):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([data.dict()])

        # The pipeline handles preprocessing internally
        prediction = model.predict(input_df)[0]

        return {"predicted_price": round(prediction, 2)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
