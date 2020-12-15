import pickle
import json
import numpy as np

__data_columns = None
__model = None


def load_saved_model():
    model = None

    global __data_columns
    global __model
    with open("./notebook/columns.json") as f:
        __data_columns = json.load(f)['data_columns']

    with open("./notebook/real_estate_model.pickle", 'rb') as f:
        __model = pickle.load(f)
def get_estimated_price(neighborhood, area, rooms, suites, bathrooms, parkings):
    try:
        loc_index = __data_columns.loc_index(neighborhood.lower())
    except:
        loc_index = -1

    
    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = rooms
    x[2] = suites
    x[3] = bathrooms
    x[4] = parkings
    
    
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],3)




if __name__ == "__main__":
    load_saved_model()
    print(get_estimated_price('JP', 140, 3, 1, 4, 1))
