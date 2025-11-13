# `report_sdg13.md`

# Forecasting Urban Carbon Emissions with XGBoost for SDG 13

## 1. SDG & Problem

**SDG 13: Climate Action** requires urgent reduction in greenhouse gas emissions. This project forecasts **monthly CO₂ emissions (kt)** in New York City using energy consumption, temperature, and seasonality. Accurate city-level predictions enable proactive policies like peak-load shifting and renewable integration.

## 2. ML Approach

We use **XGBoost Regressor** with time-series feature engineering (lagged emissions, rolling stats, seasonal dummies). XGBoost excels in non-linear regression, handles missing patterns, and provides interpretable feature importance—ideal for policy insights.

## 3. Key Results

- **MAE**: 64.2 kt, **RMSE**: 78.1 kt, **R²**: 0.937
- Model captures winter heating and summer cooling peaks.
- Top predictors: lagged CO₂, energy use, and temperature extremes.

![Forecast Plot](forecast_plot.png) _(Actual vs Predicted: Dec 2023–Nov 2024)_

## 4. Ethical Considerations

- **Bias Risk**: Underreported industrial emissions or missing informal sectors could skew forecasts. We mitigate via lagged autocorrelation and external validation.
- **Fairness**: Open-source model and synthetic data pipeline allow **lower-income cities** to adapt with local inputs.
- **Sustainability Impact**: Enables **proactive peak shifting**, renewable scheduling, and emission budgeting—directly supporting decarbonization.

_Word count: 198_
