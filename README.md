House Price Prediction

This project provides a machine learning model for predicting house prices based on input features. It includes a Flask API for serving predictions and is deployed using Render.

🚀 Features

Machine Learning Model: Trained regression-based model for accurate price estimation.

REST API: Flask-based API for real-time predictions.

Deployment: Hosted on Render for easy accessibility.

Model Versioning: Tracks improvements using DVC or MLflow.
Frontend UI: Simple web interface to interact with the model.

📦 Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor

Create a Virtual Environment
python -m venv venv
venv\Scripts\activate 

Install Dependencies
pip install -r requirements.txt

Run the Flask API Locally
python app.py
The API will be available at: http://127.0.0.1:5000/

Test API Using Postman: Send a POST request to http://127.0.0.1:5000/predict with JSON data:

{
    "feature1": 1200,
    "feature2": 3,
    "feature3": 2
}

Deploy on Render

1.Push your code to GitHub.
2.Create a new Render Web Service.
3.Connect your repository and select Flask.
4.Set the Start Command: python app.py
5.Deploy and test the API.

Model Versioning:
To track model changes, you can use DVC 
dvc init
dvc add model.pkl
git add .dvc/model.pkl.dvc

FrontEnd:
Run the frontend.py file Cell to showcase the UI of the Model.

-------------------------------------------------------------------------------------------------------------
License
This project is open-source under the MIT License.
