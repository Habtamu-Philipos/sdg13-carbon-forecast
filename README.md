# NYC CO₂ Emissions Forecaster – SDG 13

**UN SDG 13: Climate Action**  
Predicts **monthly CO₂ emissions (kt)** for New York City using energy consumption, temperature, and seasonality.

---

## Features
- **XGBoost Regressor** (R² = 0.94, MAE = 64 kt)
- **Interactive Streamlit app** (6‑month forecast)
- Full notebook, model, and synthetic data

---

## How to Run (Windows)

```cmd
py -m pip install -r requirements.txt
py -m jupyter notebook          # Run sdg13_carbon_forecast.ipynb
py -m streamlit run app.py      # Launch dashboard
