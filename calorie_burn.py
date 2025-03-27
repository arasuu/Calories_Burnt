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
st.title("Calorie Burn Predictor 🔥")

st.text_input("Enter your name (optional)")

with st.form("user_input"):
    st.header("Personal Details")
    gender = st.radio("Gender", ["male", "female"])
    age = st.slider("Age", 10, 100, 25)
    height = st.number_input("Height (cm)", 100, 250, 170)
    weight = st.number_input("Weight (kg)", 30, 200, 70)
    
    st.header("Exercise Session")
    duration = st.slider("Duration (minutes)", 1, 120, 30)
    heart_rate = st.number_input("Heart Rate (bpm)", 50, 200, 100)
    body_temp = st.number_input("Body Temp (°C)", 35.0, 42.0, 37.0)
    
    if st.form_submit_button("Predict Calories"):
        # Create DataFrame with correct columns
        input_data = pd.DataFrame([[
            age, height, weight, duration, heart_rate, body_temp
        ]], columns=[
            "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"
        ])
        
        # Encode Gender: Add 'male' column
        input_data["male"] = 1 if gender == "male" else 0
        
        

        
        # Reorder columns to match model's expected order
        expected_columns = ["male", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"]
        input_data = input_data[expected_columns]

# Check if model is loaded
if model:
    expected_features = model.feature_names_in_
    #st.write("Expected features:", expected_features)
    if not input_data.empty:
        st.write("Input data preview:", input_data.head())  # Display input data preview
        
    try:
        # Raw prediction
        calories = model.predict(input_data)[0]  
        st.subheader(f"Estimated Burn: {calories:.0f} kcal")
        st.progress(min(int(calories / 10), 100))  # Simple visual

       
        st.success(f" {calories:.0f} kcal burn!!!  Keep grinding! 🔥 ")
        
    except Exception as e:
        st.error(f"Prediction failed: {e}")
else:
    st.warning("⚠️ Model is not available. Please check the model file.")
