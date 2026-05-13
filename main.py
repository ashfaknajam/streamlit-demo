# Imported Libraries
import pickle
import streamlit as st
import numpy as np
st.title("Flower Classification App")

with open("model.pkl", "rb") as f:
    lr_model = pickle.load(f)
sl =st.slider("Insert a Sepal Length",0,10,1)
sw =st.slider("Insert a Sepal Width",0,10,1)
pl =st.slider("Insert a Petal Length",0,10,1)
pw =st.slider("Insert a Petal Width",0,10,1)

# Load the model from the file
if st.button("Predict"):
    pred = lr_model.predict(np.array([[sl,sw,pl,pw]]))
    st.write("The flower is: ", pred[0])
