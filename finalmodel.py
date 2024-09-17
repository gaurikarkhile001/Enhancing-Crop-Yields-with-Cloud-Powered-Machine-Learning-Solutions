import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the training and testing datasets
train_data = pd.read_csv('train_crop_recommendation_scaled.csv')
test_data = pd.read_csv('test_crop_recommendation_scaled.csv')

# Separate features and labels for training and testing
X_train = train_data[['N', 'P', 'K', 'temperature', 'ph', 'rainfall']]
y_train = train_data['label']
X_test = test_data[['N', 'P', 'K', 'temperature', 'ph', 'rainfall']]
y_test = test_data['label']

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the training features
X_train_scaled = scaler.fit_transform(X_train)
# Transform the testing features using the same scaler
X_test_scaled = scaler.transform(X_test)

# Initialize the Random Forest model
rf_model = RandomForestClassifier()

# Train the Random Forest model
rf_model.fit(X_train_scaled, y_train)

# Make predictions on the testing dataset
y_pred = rf_model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Random Forest Test Accuracy: {accuracy:.4f}')

# Save the trained Random Forest model and scaler
joblib.dump(rf_model, 'random_forest_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model and scaler saved successfully.")
