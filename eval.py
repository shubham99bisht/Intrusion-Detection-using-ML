import pandas as pd
import numpy as np
from keras.models import model_from_json

# load the test data from disk
test_adta = np.load("test.npy")
# print(test.shape)

# load the trained model.sav from disk
def model():
    filename = "model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model

autoencoder = model()
predictions = autoencoder.predict(test)
print(predictions[0])