import streamlit as st
import pickle
import pandas as pd


# Load model
with open('finalized_model.pkl', 'rb') as f:
    model = pickle.load(f)

# App UI
st.title("Calorie Burn Predictor 🔥")

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
                
        # Predict
        calories = model.predict(input_data)[0]
        st.success(f"Predicted Calories Burned: {calories:.0f} kcal")

test_data = pd.DataFrame([[1, 30, 175, 70, 30, 120, 37.0]], 
                        columns=['Gender','Age','Height','Weight',
                                'Duration','Heart_Rate','Body_Temp'])
try:
    st.write("Test prediction result:", model.predict(test_data)[0])
except Exception as e:
    st.error(f"Test failed: {str(e)}")


