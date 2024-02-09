#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# test_app.py
import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "index" in response.text.lower()


def test_predict_class():
    # un client qui se trouve dans le dataset
    client_id = 100001
    response = client.get(f"/predict/{client_id}")
    assert response.status_code == 200
    data = response.json()
    assert "client_id" in data
    assert "predicted_class" in data

def test_predict_class_nonexistent_client():
    # Test avec un client_id qui n'existe pas
    client_id = 1000
    response = client.get(f"/predict/{client_id}")
    assert response.status_code == 200
    data = response.json()
    assert "error" in data

