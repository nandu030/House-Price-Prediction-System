import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_loc_names():
    return __locations

def get_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations
    global __model

    try:
        with open("./artifacts/columns.json", "r") as file:
            __data_columns = json.load(file)['data_columns']
            __locations = __data_columns[3:]

        with open('./artifacts/house_price_prediction_model.pickle', 'rb') as file:
            __model = pickle.load(file)
        print("Model loaded successfully")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except pickle.UnpicklingError as e:
        print(f"Pickle file is corrupted or not a valid pickle file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Loading done")

if __name__ == "__main__":

    get_saved_artifacts()
    print(get_loc_names())
    try:
        print(get_estimated_price('kalhalli', 1000, 2, 2))
    except AttributeError as e:
        print(f"Model is not loaded properly: {e}")
