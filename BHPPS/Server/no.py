import pickle
import numpy as np

try:
    with open('./artifacts/house_price_prediction_model.pickle', 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully")
except pickle.UnpicklingError as e:
    print(f"Pickle file is corrupted or not a valid pickle file: {e}")
except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
