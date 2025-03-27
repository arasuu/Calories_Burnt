import streamlit as st
import pandas as pd
import pickle
import sys
import os
# ---- XGBoost Import with Clear Error Message ----
try:
    from xgboost import XGBRegressor
except ImportError as e:
    st.error(f"""
    ❌ Critical Error: XGBoost not installed!
    ========================================
    Please add 'xgboost>=2.0.0' to requirements.txt
    Current Python path: {sys.path}
    """)
    st.stop()  # Halt the app completely

# ---- Model Loading ----
@st.cache_resource
def load_model():
    try:
        with open('calorie_model.pkl', 'rb') as f:
            model = pickle.load(f)
            
            # Verify the loaded model is actually an XGBoost model
            if "xgboost" not in str(type(model)).lower():
                st.error("⚠️ Loaded model is not an XGBoost model!")
                return None
                
            return model
    except Exception as e:
        st.error(f"""
        🚨 Model Loading Failed
        ======================
        Error: {str(e)}
        Make sure:
        1. calorie_model.pkl exists
        2. It's a valid XGBoost model
        3. File is in the same directory
        """)
        return None

# ---- Streamlit UI ----
st.title("🔥 Calorie Burn Predictor")
model = load_model()

if model:
    with st.form("input_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            gender = st.radio("Gender", ["Male", "Female"], index=0)
            age = st.slider("Age", 10, 100, 30)
            height = st.number_input("Height (cm)", 100, 250, 175)
            
        with col2:
            weight = st.number_input("Weight (kg)", 30, 200, 70)
            duration = st.slider("Duration (mins)", 1, 300, 30)
            heart_rate = st.slider("Heart Rate (bpm)", 50, 200, 120)
        
        if st.form_submit_button("Calculate Calories"):
            try:
                input_data = pd.DataFrame({
                    'Gender': [1 if gender == "Male" else 0],
                    'Age': [age],
                    'Height': [height],
                    'Weight': [weight],
                    'Duration': [duration],
                    'Heart_Rate': [heart_rate]
                })
                
                calories = model.predict(input_data)[0]
                st.success(f"**Estimated Calories Burned:** {calories:.0f} kcal")
                
            except Exception as e:
                st.error(f"Prediction failed: {str(e)}")
else:
    st.warning("App cannot run without a valid model")
