import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load the existing model
model = pickle.load(open("crop_recommendation_model.pkl", "rb"))

# Start Flask API
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/predict", methods=["POST"])
def predict():
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
    app.run(debug=True, port=5000)
