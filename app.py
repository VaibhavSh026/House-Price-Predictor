from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Placeholder for model prediction logic
    return jsonify({"message": "Prediction received", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
