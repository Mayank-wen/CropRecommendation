# Crop Recommendation API

This is a Flask-based API that predicts the best crop to grow based on soil and environmental factors.

## Features
- Accepts soil nutrient levels (N, P, K), temperature, humidity, pH, and rainfall as input.
- Uses a pre-trained machine learning model for crop recommendation.
- CORS enabled for cross-origin requests.

## Installation

### Prerequisites
- Python 3.x
- Flask
- Flask-CORS
- Scikit-learn
- Pickle (for model loading)
- 
### Health Check
- **Endpoint:** `/`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "status": "ok",
    "message": "Crop Recommendation API is running"
  }
  ```

### Predict Crop
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Request Body (JSON):**
  ```json
  {
    "N": 50,
    "P": 30,
    "K": 40,
    "temperature": 30,
    "humidity": 60,
    "pH": 6.5,
    "rainfall": 120
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "recommended_crop": "wheat",
    "error": null
  }
  ```

## Deployment
https://croprecommendation-zblr.onrender.com
## Testing
You can test the API using:
- **cURL:**
  ```bash
  curl -X POST "https://your-api-url.onrender.com/predict" \
       -H "Content-Type: application/json" \
       -d '{"N":50, "P":30, "K":40, "temperature":30, "humidity":60, "pH":6.5, "rainfall":120}'
  ```
- **PowerShell:**
  ```powershell
  $body = @{ N = 50; P = 30; K = 40; temperature = 30; humidity = 60; pH = 6.5; rainfall = 120 } | ConvertTo-Json -Depth 3
  Invoke-RestMethod -Uri "https://your-api-url.onrender.com/predict" -Method Post -ContentType "application/json" -Body $body
  ```
- **Postman**: Send a `POST` request with JSON input to `/predict`.


