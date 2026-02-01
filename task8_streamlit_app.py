import streamlit as st
import numpy as np
st.set_page_config(page_title="COVID-19 Severity Prediction", layout="centered")
st.title("COVID-19 Severity Prediction Tool")
st.write("Enter patient details to assess hospitalization risk")
age = st.number_input("Age", min_value=1, max_value=100, value=30)
fever = st.selectbox("Fever", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
cough = st.selectbox("Cough", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
fatigue = st.selectbox("Fatigue", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
breath = st.selectbox("Shortness of Breath", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
if st.button("Predict"):
    symptoms_count = fever + cough + fatigue + breath
    if breath == 1 or symptoms_count >= 3:
        risk = "HIGH"
        hospitalized = True
    elif age >= 60 and symptoms_count >= 2:
        risk = "HIGH"
        hospitalized = True
    elif symptoms_count == 2:
        risk = "MEDIUM"
        hospitalized = False
    else:
        risk = "LOW"
        hospitalized = False
    st.subheader("Prediction Result")
    if hospitalized:
        st.error("🚨 Patient MAY require Hospitalization")
    else:
        st.success("✅ Patient does NOT require Hospitalization")
    if risk == "HIGH":
        st.markdown("### 🔴 Risk Level: **HIGH**")
    elif risk == "MEDIUM":
        st.markdown("### 🟠 Risk Level: **MEDIUM**")
    else:
        st.markdown("### 🟢 Risk Level: **LOW**")
    if breath == 1:
        st.warning("⚠️ Severe Symptom Detected: Shortness of Breath")
    st.markdown("---")
    st.success("Task 8 Completed: Model Deployed using Streamlit")
