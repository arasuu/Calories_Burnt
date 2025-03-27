import streamlit as st
import pickle
import pandas as pd

# Load model with error handling
try:
    with open('finalized_model.pickle', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None

# Minimal UI
st.title("⚡ Quick Calorie Check")

# Only essential inputs
col1, col2 = st.columns(2)
with col1:
    duration = st.slider("Minutes", 1, 120, 30)
with col2: 
    heart_rate = st.number_input("Heart Rate (bpm)", 50, 200, 100)

# Check if model is loaded
if model:
    expected_features = model.feature_names_in_
    st.write("Expected features:", expected_features)

    # When user presses the button
    if st.button("Predict"):
        # Prepare the input data to match the expected features
        input_data = pd.DataFrame({
            'Duration': [duration],
            'Heart_Rate': [heart_rate],
            # You can add any other required features here as per the model's needs
        })

        # Ensure the input data columns match the model's expected columns
        input_data = input_data[expected_features]

        try:
            # Raw prediction
            calories = model.predict(input_data)[0]
            st.subheader(f"Estimated burn: {calories:.0f} kcal")
            st.progress(min(int(calories / 10), 100))  # Simple visual
        except Exception as e:
            st.error(f"Prediction failed: {e}")
else:
    st.warning("⚠️ Model is not available. Please check the model file.")
