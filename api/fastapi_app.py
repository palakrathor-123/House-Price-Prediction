from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Files main directory mein hain, isliye ../ use kiya hai
model = pickle.load(open('../model.pkl', 'rb'))
le = pickle.load(open('../encoder.pkl', 'rb'))

class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int

@app.post("/predict")
def predict(data: HouseData):
    loc_encoded = le.transform([data.location])[0]
    features = np.array([[data.area, data.bedrooms, data.bathrooms, loc_encoded, data.age]])
    prediction = model.predict(features)
    return {"predicted_price": round(prediction[0], 2)}