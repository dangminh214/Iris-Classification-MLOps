# Iris Classification

A simple MLOps project using Docker and FastAPI to deploy a machine learning model for predicting Iris species.

## Dataset

This project is based on the [Iris Dataset](https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html), a well-known dataset in machine learning.

## Installation & Setup

### Prerequisites
- Python 3.8+
- Docker (optional for containerized deployment)
- FastAPI
- Scikit-learn
- Requests

### Running with Docker(Preferred method)

1. Build the Docker image:
   ```sh
   docker build -t app .
   ```
2. Run the container:
   ```sh
   docker run -p 8888:8888 app
   ```
3. Run User client using Streamlit
  ```bash
  streamlit run client.py 
  ```

### Running Locally

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   docker build -t app_ml .
   ```
3. Start the FastAPI server:
   ```sh
   uvicorn app:app --host 0.0.0.0 --port 8888
   ```
4. Open API documentation in your browser:
   - Swagger UI: [http://127.0.0.1:8888/docs](http://127.0.0.1:8888/docs)
   - Redoc: [http://127.0.0.1:8888/redoc](http://127.0.0.1:8888/redoc)
5. Run User client using Streamlit
  ```bash
  streamlit run client.py 
  ```

## API Endpoints

### **POST** `/predict`
- Predicts the class of the given Iris flower sample.
- **Request Body (JSON):**
  ```json
  {
    "features": [5, 6, 7, 8]
  }
  ```
- **Response:**
  ```json
  {
    "prediction": "Iris-Virginica"
  }
  ```

### **GET** `/`
- Provides information about the API.
- **Response:**
  ```json
  {
    "message": "Welcome to the Iris Classification API!"
  }
  ```

## Contributing
Feel free to open issues or submit pull requests for improvements!

## License
This project is licensed under the MIT License.
