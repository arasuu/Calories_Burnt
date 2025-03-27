import streamlit as st
import pandas as pd
import xgboost as xgb
import pickle
import os

# Load model with better error handling
@st.cache_resource
def load_model():
    try:
        # Try both .pkl and .model extensions
        if os.path.exists('finalized_model.pkl'):
            with open('finalized.pkl', 'rb') as f:
                return pickle.load(f)
        elif os.path.exists('model.model'):
            return xgb.Booster(model_file='model.model')
        else:
            st.error("Model file not found. Please ensure either 'xgboost_calorie_model.pkl' or 'model.model' exists.")
            return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

model = load_model()

st.title('Calorie Expenditure Prediction')
st.write('Predict calories burned based on exercise metrics')

# Input form
with st.form('input_form'):
    col1, col2 = st.columns(2)
    
    with col1:
        st.header('User Information')
        gender = st.radio('Gender', ['male', 'female'])
        age = st.number_input('Age', min_value=10, max_value=100, value=30)
        height = st.number_input('Height (cm)', min_value=100.0, max_value=250.0, value=170.0)
        weight = st.number_input('Weight (kg)', min_value=30.0, max_value=200.0, value=70.0)
    
    with col2:
        st.header('Exercise Metrics')
        duration = st.number_input('Duration (minutes)', min_value=1.0, max_value=300.0, value=30.0)
        heart_rate = st.number_input('Heart Rate (bpm)', min_value=50.0, max_value=200.0, value=100.0)
        body_temp = st.number_input('Body Temperature (°C)', min_value=35.0, max_value=43.0, value=37.0)
    
    submitted = st.form_submit_button('Predict Calories')

if submitted and model is not None:
    try:
        # Create DataFrame with exact feature names used during training
        input_data = pd.DataFrame([[gender, age, height, weight, duration, heart_rate, body_temp]],
                                 columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])
        
        # Convert gender to numerical (important!)
        input_data['Gender'] = input_data['Gender'].map({'male': 1, 'female': 0})
        
        # For XGBoost model (different handling for sklearn API vs native XGBoost)
        if isinstance(model, xgb.XGBRegressor):
            calories = model.predict(input_data)[0]
        else:  # Native XGBoost booster
            dmatrix = xgb.DMatrix(input_data)
            calories = model.predict(dmatrix)[0]
        
        st.success(f'Predicted Calories Burned: {calories:.2f} kcal')
        
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
