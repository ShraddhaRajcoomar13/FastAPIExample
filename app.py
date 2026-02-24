#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.joblib")

class IrisInput(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(data: IrisInput):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}

