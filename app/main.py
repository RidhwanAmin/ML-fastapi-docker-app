from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str

class Input(BaseModel):
    TOTGAS: float 
    ECDBIT: float 
    ROP_AVG: float 


class PredictionOut(BaseModel):
    prediction: str

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(data: Input):
    data = data.dict()
    TOTGAS=data['TOTGAS']
    ECDBIT=data['ECDBIT']
    ROP_AVG=data['ROP_AVG']
    
    prediction = predict_pipeline(([[TOTGAS,ECDBIT,ROP_AVG]]))
    return {"prediction": prediction[0]}
