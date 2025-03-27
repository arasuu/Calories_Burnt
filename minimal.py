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

if st.form_submit_button("Predict Calories"):
    try:
        # 1. Create proper input DataFrame
        input_dict = {
            'User_ID': [user_id],
            'Gender': [1 if gender == "male" else 0],
            'Age': [age],
            'Height': [height],
            'Weight': [weight],
            'Duration': [duration],
            'Heart_Rate': [heart_rate],
            'Body_Temp': [body_temp]
        }
        
        # 2. Convert to DataFrame with correct column order
        input_df = pd.DataFrame(input_dict)[model.feature_names_in_]
        
        # 3. Type conversion
        input_df = input_df.astype(float)
        
        # 4. Debug check (remove after confirming it works)
        st.write("Input being sent to model:", input_df)
        
        # 5. Predict
        calories = model.predict(input_df)[0]
        st.success(f"Predicted: {calories:.0f} kcal")
        
    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")
        st.write("🔍 Debug Info:")
        st.write("Model expects these features:", model.feature_names_in_)
        st.write("Your input features:", input_dict.keys())
    
    # Basic output
    st.subheader(f"Estimated burn: {calories:.0f} kcal")
    st.progress(min(int(calories/10), 100))  # Simple visual
