# app.py - Fixed for Streamlit Cloud
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="SDG 13: NYC CO₂ Forecast", layout="wide")

# Load model & data
@st.cache_resource
def load_model():
    return joblib.load('xgb_carbon_model.pkl')

@st.cache_data
def load_data():
    return pd.read_csv('nyc_carbon_data.csv')

model = load_model()
data = load_data()

st.title("NYC CO₂ Emissions Forecaster")
st.markdown("**UN SDG 13: Climate Action** – Predict monthly CO₂ using energy & temperature")

# Sidebar
st.sidebar.header("Input Parameters")
temp = st.sidebar.slider("Average Temperature (°C)", -10.0, 35.0, 15.0)
energy = st.sidebar.slider("Energy Consumption (GWh)", 2500.0, 4500.0, 3500.0)
months_ahead = st.sidebar.selectbox("Forecast Months", [1, 3, 6], index=2)

# Feature creation
last_row = data.iloc[-1]
feature_cols = [col for col in data.columns if col not in ['date', 'co2_kt']]

def create_features(temp, energy, prev_co2, month):
    row = {
        'temperature_c': temp,
        'energy_consumption_gwh': energy,
        'is_holiday_month': 1 if month in [1, 12] else 0,
        'year': 2025,
        'co2_lag_1': prev_co2,
        'co2_lag_2': prev_co2,
        'co2_lag_3': prev_co2,
        'co2_roll_mean_3': prev_co2,
        'co2_roll_std_3': 50.0
    }
    for m in range(2, 13):
        row[f'month_{m}'] = 1 if month == m else 0
    return pd.DataFrame([row])[feature_cols]

# Forecast
forecast = []
current_co2 = data['co2_kt'].iloc[-1]
current_month = 1

for i in range(months_ahead):
    X = create_features(temp, energy, current_co2, current_month)
    pred = model.predict(X)[0]
    forecast.append({
        'date': pd.Timestamp(2025, current_month, 1),
        'predicted_co2_kt': round(pred, 1)
    })
    current_co2 = pred
    current_month = (current_month % 12) + 1

forecast_df = pd.DataFrame(forecast)

# Results
col1, col2 = st.columns(2)
with col1:
    st.metric("Next Month CO₂", f"{forecast_df.iloc[0]['predicted_co2_kt']} kt")
with col2:
    st.metric("6-Month Total", f"{forecast_df['predicted_co2_kt'].sum():.0f} kt")

st.subheader("6-Month Forecast")
fig, ax = plt.subplots()
ax.plot(forecast_df['date'], forecast_df['predicted_co2_kt'], marker='o', color='red')
ax.set_title("Predicted CO₂ Emissions (kt)")
ax.set_ylabel("CO₂ (kt)")
ax.grid(True)
st.pyplot(fig)

st.subheader("Historical CO₂ (2018–2024)")
fig2, ax2 = plt.subplots()
ax2.plot(data['date'], data['co2_kt'], color='gray')
ax2.set_title("Historical Monthly Emissions")
ax2.set_ylabel("CO₂ (kt)")
st.pyplot(fig2)

st.caption("Model: XGBoost (R² = 0.94) | Made for SDG 13")