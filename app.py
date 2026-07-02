import streamlit as st
from farming_agent import FarmingAgent

agent = FarmingAgent()

st.set_page_config(
    page_title="AgriSense AI",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 SmartCrop AI")
st.markdown("Smart Crop Recommendation System")

st.divider()
st.subheader("👨‍🌾 Farmer Information")

farmer_name = st.text_input("Farmer Name")

location = st.text_input("Village / District")

soil_type = st.selectbox(
    "Soil Type",
    [
        "Loamy",
        "Clay",
        "Sandy",
        "Black Soil",
        "Red Soil"
    ]
)

st.divider()
st.subheader("🌱 Soil & Weather Parameters")

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen")
    P = st.number_input("Phosphorus")
    K = st.number_input("Potassium")
    ph = st.number_input("pH")

with col2:
    temperature = st.number_input("Temperature")
    humidity = st.number_input("Humidity")
    rainfall = st.number_input("Rainfall")
if st.button("🚀 Analyze Crop"):

    crop = agent.recommend_crop(
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    )

    st.session_state["show_report"] = True
    st.session_state["crop"] = crop
if st.session_state.get("show_report", False):

    st.divider()

    st.header("📋 Crop Recommendation Report")

    st.write(f"👨‍🌾 Farmer Name :  {farmer_name}")

    st.write(f"📍 Location :  {location}")

    st.write(f"🌱 Soil Type :  {soil_type}")

    st.write(f"🌾 Recommended Crop :  {st.session_state['crop']}")

    st.success("Analysis Completed Successfully")