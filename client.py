import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px

# FastAPI endpoint URL
# API_URL = "http://127.0.0.1:8888"
API_URL = "https://iris-classification-mlops-production.up.railway.app"

# Page config
st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
    }
    .stNumberInput>div>div>input {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🌸 Iris Flower Classification")
st.markdown("""
    This application predicts the species of an Iris flower based on its measurements.
    Enter the flower's characteristics below and click 'Predict' to see the result.
    """)

# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    # Input section with a nice container
    with st.container():
        st.subheader("📏 Enter Flower Measurements")
        
        # Create two rows of inputs
        col1_1, col1_2 = st.columns(2)
        with col1_1:
            sepal_length = st.number_input(
                "Sepal Length (cm)",
                min_value=0.0,
                step=0.1,
                format="%.1f",
                help="Length of the sepal in centimeters"
            )
            petal_length = st.number_input(
                "Petal Length (cm)",
                min_value=0.0,
                step=0.1,
                format="%.1f",
                help="Length of the petal in centimeters"
            )
        
        with col1_2:
            sepal_width = st.number_input(
                "Sepal Width (cm)",
                min_value=0.0,
                step=0.1,
                format="%.1f",
                help="Width of the sepal in centimeters"
            )
            petal_width = st.number_input(
                "Petal Width (cm)",
                min_value=0.0,
                step=0.1,
                format="%.1f",
                help="Width of the petal in centimeters"
            )

    # Predict button with emoji
    if st.button("🔮 Predict Species", type="primary"):
        data = {"features": [sepal_length, sepal_width, petal_length, petal_width]}
        response = requests.post(f"{API_URL}/predict", data=json.dumps(data), headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            prediction = response.json()['message']
            st.success(f"### Predicted Species: {prediction}")
            
            # Add some visual feedback
            if "setosa" in prediction.lower():
                st.image("https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg", 
                        caption="Iris Setosa", width=200)
            elif "versicolor" in prediction.lower():
                st.image("https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg", 
                        caption="Iris Versicolor", width=200)
            elif "virginica" in prediction.lower():
                st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg", 
                        caption="Iris Virginica", width=200)
        else:
            st.error("❌ Error: Unable to get prediction. Please check the API server.")

with col2:
    # Info section
    with st.container():
        st.subheader("ℹ️ About")
        if st.button("Get API Information"):
            response = requests.get(f"{API_URL}/")
            
            if response.status_code == 200:
                st.info(response.json()["message"])
            else:
                st.error("❌ Error: Unable to get API info.")

    # Add some educational content
    with st.container():
        st.subheader("📚 Iris Species")
        st.markdown("""
        The Iris dataset contains three species:
        - Iris Setosa
        - Iris Versicolor
        - Iris Virginica
        """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and FastAPI - Dang Minh Nguyen")
        
