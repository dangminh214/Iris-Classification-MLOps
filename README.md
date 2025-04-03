
# Iris Classification

A simple MLOps project demonstrating how to deploy a machine learning model for Iris species prediction using Docker and FastAPI.

Live demo:  
[**Iris Classification App**](https://iris-classification-dang-minh.streamlit.app/)

## Dataset

This project utilizes the [Iris Dataset](https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html), a classic dataset in machine learning that contains 150 samples of Iris flowers, each characterized by four features: sepal length, sepal width, petal length, and petal width.

## Installation & Setup

### Prerequisites

Before setting up the project, make sure you have the following tools installed:

- Python 3.8+  
- Docker (Optional for containerized deployment)  
- FastAPI  
- Scikit-learn  
- Requests  
- Streamlit (for running the client-side application)

### Running with Docker (Preferred Method)

1. **Build the Docker image**  
   Build the Docker image for the application.
   ```bash
   docker build -t iris-classification-app .
   ```

2. **Run the Docker container**  
   Start the server inside a Docker container.
   ```bash
   docker run -p 8888:8888 iris-classification-app
   ```

3. **Run the client-side application**  
   Use Streamlit to run the client application.
   ```bash
   streamlit run client.py
   ```

### Running Locally (Without Docker)

1. **Clone the repository**  
   Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies**  
   Install the required Python dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI server**  
   Run the FastAPI server to serve the model.
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8888
   ```

4. **Access API Documentation**  
   Open the following API documentation in your browser:
   - Swagger UI: [http://127.0.0.1:8888/docs](http://127.0.0.1:8888/docs)
   - Redoc: [http://127.0.0.1:8888/redoc](http://127.0.0.1:8888/redoc)

5. **Run the client-side application**  
   Use Streamlit to run the client application.
   ```bash
   streamlit run client.py
   ```

## API Endpoints

### **POST** `/predict`

Predicts the Iris flower species based on the given feature values.

- **Request Body (JSON):**
  ```json
  {
    "features": [5.1, 3.5, 1.4, 0.2]
  }
  ```
- **Response:**
  ```json
  {
    "prediction": "Iris-setosa"
  }
  ```

### **GET** `/`

Provides a welcome message with information about the API.

- **Response:**
  ```json
  {
    "message": "Welcome to the Iris Classification API!"
  }
  ```

## Deployment

- **Remote Model & API Deployment**  
  The FastAPI model and server have been deployed remotely on [Railway](https://railway.app):
  [**Iris Classification API (Production)**](https://iris-classification-mlops-production.up.railway.app)

- **Remote Streamlit Client Deployment**  
  The client-side application is deployed using Streamlit:
  [**Iris Classification Client**](https://iris-classification-dang-minh.streamlit.app/)

## Contributing

Contributions are welcome! If you find any issues or want to suggest improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.