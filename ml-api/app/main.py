from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI(title="ML Model API")

class InputData(BaseModel):
    value: int

@app.get("/")
def home():
    return {"message": "ML Model API is running"}

@app.post("/predict")
def predict_api(data: InputData):
    result = predict(data.value)
    return {"input": data.value, "prediction": result}