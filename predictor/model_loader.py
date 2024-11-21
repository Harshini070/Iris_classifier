# predictor/model_loader.py
import joblib
import os

# Define the path to the savedmodels directory
base_dir = os.path.dirname(os.path.dirname(__file__))  # This goes up one level to the project directory
model_path = os.path.join(base_dir, 'savedmodels', 'iris_model.joblib')

# Load the pre-trained model
model = joblib.load(model_path)
