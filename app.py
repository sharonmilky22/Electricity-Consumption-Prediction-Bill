import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("Electricity_model.pkl")

# App title
st.title("Electricity Bill Prediction")

# Input values
fan = st.number_input("Fan", min_value=0.0)
refrigerator = st.number_input("Refrigerator", min_value=0.0)
air_conditioner = st.number_input("Air Conditioner", min_value=0.0)
television = st.number_input("Television", min_value=0.0)
monitor = st.number_input("Monitor", min_value=0.0)
motor_pump = st.number_input("Motor Pump", min_value=0.0)
monthly_hours = st.number_input("Monthly Hours", min_value=0.0)
tariff_rate = st.number_input("Tariff Rate", min_value=0.0)

# Prediction
if st.button("Predict Electricity Bill"):

    data = np.array([[fan, refrigerator, air_conditioner,
                      television, monitor, motor_pump,
                      monthly_hours, tariff_rate]])

    prediction = model.predict(data)

    st.success(f"Predicted Electricity Bill: {prediction[0]:.2f}")