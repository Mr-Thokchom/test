import streamlit as st
import pickle
import numpy as np

# Load the trained Logistic Regression model
with open('lrmodel_sustainable.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Ad Sustainable App")

# User input fields
carbon_emission = st.number_input("Carbon emission amount:", min_value=0.0, format="%f")
energy_output = st.number_input("Energy Generated:", min_value=0.0, format="%f")
renewability_index = st.number_input("Renewability Index:", min_value=0.0, format="%f")
cost_efficiency = st.number_input("Cost Efficiency:", min_value=0.0, format="%f")
# Predict button
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[carbon_emission, energy_output, renewability_index,cost_efficiency]])
    
    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    if prediction[0] == 1:
        st.success("Yes it is sustainable.")
    else:
        st.info("Need to Improve, Not sustainable")