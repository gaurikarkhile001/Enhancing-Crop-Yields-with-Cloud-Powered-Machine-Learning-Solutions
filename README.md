# Crop Recommendation System using Machine Learning and AWS

This project aims to provide accurate crop recommendations based on soil and environmental parameters using machine learning algorithms. The system is designed to assist farmers in choosing the best crops to grow in specific conditions, promoting sustainable agricultural practices.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment on AWS](#deployment-on-aws)
- [Future Work](#future-work)
- [Contributing](#contributing)

## Features
- Predicts the most suitable crop based on inputs like Nitrogen (N), Phosphorus (P), Potassium (K), temperature, pH, and rainfall.
- Implements Random Forest for accurate crop predictions.
- Utilizes AWS S3 for storage and deployment, along with AWS Lambda for serverless functionality.
- Dockerized application for easy deployment with Jenkins CI/CD pipeline.

## Technologies Used
- **Python** for backend logic and model serving.
- **Flask** for web-based API to serve predictions.
- **Machine Learning**: Random Forest model for prediction.
- **Docker** for containerization.
- **Jenkins** for continuous integration and deployment.
- **AWS Services**:
  - S3 for storage and deployment.
  - Lambda for serverless computing.
  - EC2 for scalable hosting.
  - AWS IoT Core (future work) for real-time data integration.

## Project Structure
```
├── app.py                 # Main Flask app
├── random_forest_model.pkl # Pre-trained machine learning model
├── scaler.pkl             # Data scaler for input transformation
├── templates
│   └── index.html         # Frontend HTML for user input
├── static
│   └── 2.jpg              # Background image for the web app
├── Dockerfile             # Docker configuration
├── Jenkinsfile            # CI/CD pipeline configuration
└── README.md              # Project documentation
```

## Installation

### Prerequisites
- Python 3.8+
- Flask
- Joblib
- Numpy
- AWS CLI configured with your credentials

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/gaurikarkhile001/Enhancing-Crop-Yields-with-Cloud-Powered-Machine-Learning-Solutions.git
   cd Crop-Recommendation-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   python app.py
   ```

## Usage
1. Input parameters such as Nitrogen, Phosphorus, Potassium, temperature, pH, and rainfall in the web interface.
2. Click on "Recommend Crop" to get the suggested crop.

## Deployment on AWS

### S3 Deployment
1. Create an S3 bucket and upload the application files.
2. Use AWS Lambda to configure the Flask app as a serverless function.
3. Trigger the Lambda function through API Gateway for serving crop recommendations.

### EC2 Deployment
1. Create an EC2 instance and install Docker.
2. Pull the Docker image and run the container:
   ```bash
   docker pull <your-docker-image>
   docker run -p 80:80 <your-docker-image>
   ```

## Future Work
- **Real-Time Data**: Integrate IoT sensors via AWS IoT Core for dynamic recommendations.
- **Global Reach**: Use AWS Global Infrastructure for wider access.
- **AI Optimization**: Enhance model accuracy using AWS SageMaker.
- **Serverless Scaling**: Extend serverless architecture using AWS Lambda, with S3 for storage and deployment.

