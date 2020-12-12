import tensorflow as tf
from tensorflow import keras
model = tf.keras.models.load_model('my_model.hdf5')

import streamlit as st
st.write("""
         # German Street Road Sign Prediction
         """
         )
st.write("This is a simple image classification web app to classify the road signs")
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
    img_array = keras.preprocessing.image.img_to_array(image_data)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    prediction = model.predict(img_array)
    return prediction
if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    score = tf.nn.softmax(prediction) 
    st.write("The sign corresponds to", np.argmax(score), "ClassId.")
    st.write("Confidence:",  round(100 * np.max(score), 1), "%")
