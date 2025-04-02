import streamlit as st 
import requests 
import json

# FastAPI endpoint URL
url = "http://127.0.0.1:8888/predict/"

st.title("Iris Classification with FastAPI")
st.write("Enter the feature values and get the predicted class.")

# User inputs
sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1, format="%.1f")
sepal_width = st.number_input("Sepal Width", min_value=0.0, step=0.1, format="%.1f")
petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1, format="%.1f")
petal_width = st.number_input("Petal Width", min_value=0.0, step=0.1, format="%.1f")

if st.button("Predict"):
    data = {"features": [sepal_length, sepal_width, petal_length, petal_width]}
    response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        st.success(f"Predicted class: {response.json()["message"]}")
    else:
        st.error("Error: Unable to get prediction. Check API server.")
