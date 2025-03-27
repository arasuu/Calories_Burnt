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

with st.form("user_input"):
    st.header("Personal Details")
    user_id = st.number_input("User ID", min_value=10000000, max_value=99999999, value=14733363)
    gender = st.radio("Gender", ["male", "female"])
    age = st.slider("Age", 10, 100, 25)
    height = st.number_input("Height (cm)", 100, 250, 170)
    weight = st.number_input("Weight (kg)", 30, 200, 70)
    
    st.header("Exercise Session")
    duration = st.slider("Duration (minutes)", 1, 120, 30)
    heart_rate = st.number_input("Heart Rate (bpm)", 50, 200, 100)
    body_temp = st.number_input("Body Temp (°C)", 35.0, 42.0, 37.0)
    
    if st.form_submit_button("Predict Calories"):
        input_data = pd.DataFrame([[
            user_id, gender, age, height, weight, 
            duration, heart_rate, body_temp
        ]], columns=[
            "User_ID", "Gender", "Age", "Height", "Weight",
            "Duration", "Heart_Rate", "Body_Temp"
        ])
        
        # Preprocess (add your own preprocessing steps)
        input_data["Gender"] = input_data["Gender"].map({"male": 1, "female": 0})

# Check if model is loaded
st.write("Input data type:", type(input_data))
st.write("Input data preview:", input_data.head())
st.write("Are all input values numeric?", input_data.applymap(pd.to_numeric, errors='coerce').notna().all())


if model:
    expected_features = model.feature_names_in_
    st.write("Expected features:", expected_features)

        
    #input_data = input_data[expected_features]

    try:
        # Raw prediction
        calories = model.predict(expected_features)[0]
        st.subheader(f"Estimated burn: {calories:.0f} kcal")
        st.progress(min(int(calories / 10), 100))  # Simple visual
    except Exception as e:
        st.error(f"Prediction failed: {e}")
else:
    st.warning("⚠️ Model is not available. Please check the model file.")
