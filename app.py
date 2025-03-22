# from flask import Flask, request, jsonify
# import pickle
# import pandas as pd

# # Load the trained model
# with open("house_price_model.pkl", "rb") as file:
#     model = pickle.load(file)

# # Initialize Flask app
# app = Flask(__name__)

# # Define prediction route
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         # Check if request content type is JSON
#         if not request.is_json:
#             return jsonify({"error": "Request content-type must be application/json"}), 415

#         data = request.get_json()  # Get JSON data
#         if not data:
#             return jsonify({"error": "Empty request body"}), 400

#         input_features = pd.DataFrame([data])  # Convert to DataFrame

#         # Ensure feature order matches training data
#         prediction = model.predict(input_features)[0]  # Make prediction
        
#         return jsonify({"predicted_price": round(prediction, 2)})  # Return response
#     except Exception as e:
#         return jsonify({"error": str(e)})

# # Run the app
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

try:
    with open("house_price_model.pkl", "rb") as file:
        model = pickle.load(file)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise

FEATURES = ['MSSubClass', 'LotArea', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
            'BsmtFinSF2', 'TotalBsmtSF', 'MSZoning_FV', 'MSZoning_RH', 'MSZoning_RL',
            'MSZoning_RM', 'LotConfig_CulDSac', 'LotConfig_FR2', 'LotConfig_FR3',
            'LotConfig_Inside', 'BldgType_2fmCon', 'BldgType_Duplex', 'BldgType_Twnhs',
            'BldgType_TwnhsE', 'Exterior1st_AsphShn', 'Exterior1st_BrkComm',
            'Exterior1st_BrkFace', 'Exterior1st_CBlock', 'Exterior1st_CemntBd',
            'Exterior1st_HdBoard', 'Exterior1st_ImStucc', 'Exterior1st_MetalSd',
            'Exterior1st_Plywood', 'Exterior1st_Stone', 'Exterior1st_Stucco',
            'Exterior1st_VinylSd', 'Exterior1st_Wd Sdng', 'Exterior1st_WdShing']

@app.route("/")
def home():
    return jsonify({"message": "House Price Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Empty request body"}), 400

        input_data = pd.DataFrame([data])

        for feature in FEATURES:
            if feature not in input_data.columns:
                input_data[feature] = 0

        input_data = input_data[FEATURES]
        
        prediction = model.predict(input_data)[0]

        return jsonify({"predicted_price": round(prediction, 2)})
    
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)