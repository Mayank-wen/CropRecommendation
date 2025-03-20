import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load model with error handling
try:
    model = pickle.load(open("crop_recommendation_model.pkl", "rb"))
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({
            "success": False,
            "recommended_crop": None,
            "error": "Model failed to load"
        }), 500

    try:
        data = request.json
        input_data = [[
            float(data["N"]), 
            float(data["P"]), 
            float(data["K"]), 
            float(data["temperature"]), 
            float(data["humidity"]), 
            float(data["pH"]), 
            float(data["rainfall"])
        ]]
        prediction = model.predict(input_data)
        return jsonify({
            "success": True,
            "recommended_crop": prediction[0],
            "error": None
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "recommended_crop": None,
            "error": str(e)
        }), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
