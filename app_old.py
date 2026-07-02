import streamlit as st
from farming_agent import FarmingAgent

agent = FarmingAgent()

st.title("🌾 AI Farming Assistant")

N = st.number_input("Nitrogen")
P = st.number_input("Phosphorus")
K = st.number_input("Potassium")

temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
ph = st.number_input("pH")
rainfall = st.number_input("Rainfall")

if st.button("Recommend Crop"):

    crop = agent.recommend_crop(
        N, P, K,
        temperature,
        humidity,
        ph,
        rainfall
    )

    st.success(f"Recommended Crop: {crop}")