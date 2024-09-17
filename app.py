import awsgi
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        data['N'],
        data['P'],
        data['K'],
        data['temperature'],
        data['ph'],
        data['rainfall']
    ]
    features_array = np.array([features])
    features_scaled = scaler.transform(features_array)
    prediction = model.predict(features_scaled)
    return jsonify({'crop': prediction[0]})


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})


if __name__ == '__main__':
    app.run(debug=True)
