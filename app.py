from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import logging

logging.basicConfig(filename="app.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

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

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "House Price Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            logging.warning("Empty request received.")
            return jsonify({"error": "Empty request body"}), 400

        logging.info(f"Received request: {data}")

        input_data = pd.DataFrame([data])

        for feature in FEATURES:
            if feature not in input_data.columns:
                input_data[feature] = 0

        input_data = input_data[FEATURES]

        prediction = model.predict(input_data)[0]

        response = {"predicted_price": round(prediction, 2)}
        logging.info(f"Prediction successful: {response}")

        return jsonify(response)

    except Exception as e:
        logging.error(f"Error in prediction: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
