from keras.models import load_model
import cv2
import numpy as np
import sys

filepath = sys.argv[1]

CATEGORY_MAP = {
    "Good Job": 0,
    "I love you": 1,
    "Next Slide": 2,
    "Previous Slide": 3,
    "See you later": 4,
    "Yes": 5
}

# This function returns the gesture name from its numeric equivalent 
def mapper(val):
    return CATEGORY_MAP[val]

#Load the saved model file
model = load_model("gesture-model.h5")

# Ensuring the input image has same dimensions that is used during training. 
img = cv2.imread(filepath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (225, 225))

# Predict the gesture from the input image
prediction = model.predict(np.array([img]))

gesture_numeric = np.argmax(prediction[0])
gesture_name = mapper(gesture_numeric)

print("Predicted Gesture: {}".format(gesture_name))