import streamlit as st
import pickle
import pandas as pd

# Load model
with open('finalized_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Minimal UI
st.title("⚡ Quick Calorie Check")

# Only essential inputs
col1, col2 = st.columns(2)
with col1:
    duration = st.slider("Minutes", 1, 120, 30)
with col2: 
    heart_rate = st.number_input("Heart Rate (bpm)", 50, 200, 100)

if st.button("Predict"):
    # Minimal input formatting
    # Convert all to numeric
    input_data = input_data.astype(float)
    input_data = pd.DataFrame([[duration, heart_rate]], 
                            columns=["Duration", "Heart_Rate"])

    print("Model features during training:", model.feature_names_in_)
    print("Your input columns:", input_data.columns)
    print("Input dtypes:", input_data.dtypes)
    # Raw prediction
    calories = model.predict(input_data)[0]
    
    # Basic output
    st.subheader(f"Estimated burn: {calories:.0f} kcal")
    st.progress(min(int(calories/10), 100))  # Simple visual
