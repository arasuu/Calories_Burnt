# app.py
import streamlit as st
import pandas as pd
import pickle
import os
from xgboost import XGBRegressor

# --- SETTINGS ---
st.set_page_config(
    page_title="Calorie Burn Predictor",
    page_icon="🔥",
    layout="wide"
)

# --- MODEL LOADING ---
@st.cache_resource
def load_model():
    """Load the trained XGBoost model with error handling"""
    try:
        model_path = 'finalized_model.pkl'
        if not os.path.exists(model_path):
            st.error(f"Model file not found at: {os.path.abspath(model_path)}")
            return None
            
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
            
        if not isinstance(model, XGBRegressor):
            st.error("Loaded object is not an XGBRegressor")
            return None
            
        return model
    except Exception as e:
        st.error(f"Model loading failed: {str(e)}")
        return None

# --- UI COMPONENTS ---
st.title("🔥 Calorie Burn Predictor")
st.markdown("Predict calories burned during exercise based on your metrics")

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        with st.form("user_inputs"):
            st.subheader("Personal Information")
            gender = st.radio("Gender", ["Male", "Female"], index=0, horizontal=True)
            age = st.slider("Age", 10, 100, 30)
            height = st.number_input("Height (cm)", 100.0, 250.0, 175.0, step=0.5)
            weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0, step=0.5)
            
            st.subheader("Exercise Details")
            duration = st.slider("Duration (minutes)", 1, 300, 30)
            heart_rate = st.slider("Heart Rate (bpm)", 50, 200, 120)
            body_temp = st.slider("Body Temperature (°C)", 36.0, 42.0, 37.5, step=0.1)
            
            submitted = st.form_submit_button("Calculate Calories")

# --- PREDICTION LOGIC ---
if submitted:
    model = load_model()
    if model:
        try:
            # Prepare input data
            input_data = pd.DataFrame({
                'Gender': [1 if gender == 'Male' else 0],
                'Age': [age],
                'Height': [height],
                'Weight': [weight],
                'Duration': [duration],
                'Heart_Rate': [heart_rate],
                'Body_Temp': [body_temp]
            })
            
            # Make prediction
            calories = model.predict(input_data)[0]
            
            # Display results
            st.success(f"## Estimated Calories Burned: {calories:.0f} kcal")
            
            # Visual progress bar
            max_calories = 1000  # Adjust based on your expected range
            progress = min(calories / max_calories, 1.0)
            st.progress(progress, text=f"{progress*100:.0f}% of {max_calories} kcal max")
            
            # Exercise equivalents
            st.markdown("### This is equivalent to:")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Running", f"{calories/100*1.6:.1f} km")
            with col2:
                st.metric("Cycling", f"{calories/100*4.8:.1f} km")
            with col3:
                st.metric("Swimming", f"{calories/100*0.9:.1f} km")
                
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

# --- SIDEBAR INFO ---
with st.sidebar:
    st.header("About")
    st.markdown("""
    This app predicts calories burned using:
    - XGBoost regression model
    - Exercise physiology parameters
    - Personal biometric data
    """)
    
    st.header("How to Use")
    st.markdown("""
    1. Enter your personal details
    2. Input exercise metrics
    3. Click 'Calculate Calories'
    """)
