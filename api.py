#!/usr/bin/env python
# coding: utf-8

# In[14]:


from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
from joblib import load
from sklearn.preprocessing import MinMaxScaler
import pandas as pd


# In[15]:


# Importez du modèle 

model = load('lgbm_w.joblib')

app = FastAPI()
# scale de donnees 
scaler = MinMaxScaler(feature_range = (0, 1))

class ClientInput(BaseModel):
    client_id: int

class PredictionOutput(BaseModel):
    client_id: int
    predicted_class: int
    predicted_score: float

@app.get("/predict/{client_id}")
async def predict_class(client_id: int = Path(..., title="ID du client")):
    # recuperation des caracteristiques du dataframe
    features_for_client_id = get_features_for_client_id(client_id)
    
    if features_for_client_id is not None:
        
        predicted_proba = model.predict_proba([features_for_client_id])[0]
        predicted_class = int(model.predict([features_for_client_id])[0] > 0.499)  
        predicted_score = float(predicted_proba[1])
        # la classe de sortie
        output = PredictionOutput(client_id=client_id, predicted_class=predicted_class, predicted_score=predicted_score)
        return output
    else:
        return {"error": "Client non trouvé"}

# Fonction pour récupérer les caractéristiques du client
def get_features_for_client_id(client_id):
    df=pd.read_csv('./test_app.csv')
    df=df[:50]
    # recherche du client 
    client_data = df[df['SK_ID_CURR'] == client_id].drop(columns=['SK_ID_CURR'])
    if client_data.shape[0]==1:
        scaler.fit(client_data)
        scaled_client_data = scaler.transform(client_data)
        return client_data.values[0] 
    else:
        return None

 
@app.get('/')
def index():
    return "Bonjour, c'est la page d'index"


# In[ ]:




