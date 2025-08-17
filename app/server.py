from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from app import util
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import pandas as pd


app = FastAPI()

model = joblib.load('./app/artifacts/model.joblib')

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:8000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get('/')
def root():
    return {'message': 'Bank Term Deposit Model'}

@app.post('/predict')
def predict(data: dict):
    features = pd.DataFrame([data])
    features_processed = util.engineer_features(features)
    prediction = model.predict_proba(features_processed)[:,1][0]
    percentage = f"{str(round(prediction*100, 1))}%"
    return percentage

# @app.get('/marital_status')
# async def marital_status():
#     marital = utils.get_marital_status()
#     return {'marital_status': marital}



