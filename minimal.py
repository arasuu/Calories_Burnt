import streamlit as st
import pickle
import pandas as pd

@st.cache_data
def load_model():
    with open('finalized_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

st.title("Calorie Burn Calculator 🔥")
duration = st.slider("Exercise Duration (min)", 1, 120, 30)
heart_rate = st.number_input("Heart Rate (bpm)", 60, 200, 100)

if st.button("Predict"):
    calories = model.predict([[duration, heart_rate]])[0]
    st.success(f"Estimated calories burned: {calories:.0f} kcal")
