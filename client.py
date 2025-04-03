import streamlit as st
import requests
import json

# FastAPI endpoint URL
# API_URL = "http://127.0.0.1:8888"
API_URL = "https://iris-classification-mlops-production.up.railway.app"

st.title("Iris Classification with FastAPI")
st.write("Enter the feature values and get the predicted class.")

# User inputs
sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1, format="%.1f")
sepal_width = st.number_input("Sepal Width", min_value=0.0, step=0.1, format="%.1f")
petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1, format="%.1f")
petal_width = st.number_input("Petal Width", min_value=0.0, step=0.1, format="%.1f")

# Predict button
if st.button("Predict"):
    data = {"features": [sepal_length, sepal_width, petal_length, petal_width]}
    response = requests.post(f"{API_URL}/predict", data=json.dumps(data), headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        st.success(f"Predicted class: {response.json()['message']}")
    else:
        st.error("Error: Unable to get prediction. Check API server.")

# Info button
if st.button("Info"):
    response = requests.get(f"{API_URL}/")
    
    if response.status_code == 200:
        st.info(response.json()["message"])
    else:
        st.error("Error: Unable to get API info.")
