import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("booking_model.pkl")  # Save your trained model as 'booking_model.pkl'

model = load_model()

# Load encoders and scaler
label_encoders = joblib.load("label_encoders.pkl")  # Save LabelEncoders used during training
scaler = joblib.load("scaler.pkl")  # Save StandardScaler used during training

# Define categorical and numerical feature names
categorical_features = ['gender', 'type of meal', 'room type', 'market segment', 'repeated guest']
numerical_features = ['lead time', 'arrival month', 'arrival date', 'stays in weekend nights',
                      'stays in week nights', 'adults', 'children', 'babies', 'required car parking space']

st.title("Hotel Booking Prediction App 🏨✨")
st.write("Enter the details below to check if the booking is **Confirmed** or **Canceled**")

# User inputs for features
input_data = {}

# Input fields for categorical features
for feature in categorical_features:
    options = label_encoders[feature].classes_.tolist()  # Get original categories
    input_data[feature] = st.selectbox(f"Select {feature.replace('_', ' ').title()}:", options)

# Input fields for numerical features
for feature in numerical_features:
    input_data[feature] = st.number_input(f"Enter {feature.replace('_', ' ').title()}:", min_value=0, value=1)

# Convert categorical inputs using saved encoders
for feature in categorical_features:
    input_data[feature] = label_encoders[feature].transform([input_data[feature]])[0]

# Convert to DataFrame for processing
input_df = pd.DataFrame([input_data])

# Standardize numerical features
input_df[numerical_features] = scaler.transform(input_df[numerical_features])

# Predict on user input
if st.button("Predict Booking Status"):
    prediction = model.predict(input_df)[0]
    status = "✅ Confirmed" if prediction == 1 else "❌ Canceled"
    st.subheader(f"Booking Status: {status}")

st.markdown("#### Trained using RandomForestClassifier with high accuracy!")
