import streamlit as st
import pickle
import pandas as pd

# Load model with error handling
try:
    with open('finalized_model.pkl', 'rb') as f:
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

if st.button("Predict") and model:
    # Minimal input formatting
    input_data = pd.DataFrame([[duration, heart_rate]], 
                            columns=["Duration", "Heart_Rate"])
    
    # Raw prediction
    calories = model.predict(input_data)[0]
    
    # Basic output
    st.subheader(f"Estimated burn: {calories:.0f} kcal")
    st.progress(min(int(calories / 10), 100))  # Simple visual

elif not model:
    st.warning("⚠️ Model is not available. Please check the model file.")

