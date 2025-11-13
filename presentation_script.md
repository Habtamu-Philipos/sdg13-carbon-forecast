# `presentation_script.md`

# 5-Minute Presentation Script (120 sec talk + 3 min demo)

### Slide 1: Title & SDG 13

> _"Hi! I'm building an AI tool for **SDG 13: Climate Action**. Cities emit 70% of CO₂ — we need **monthly forecasts** to act."_ > **Show**: Title + SDG logo

---

### Slide 2: The Problem & Data

> _"We predict NYC’s CO₂ using energy, temperature, and past emissions. Data is sparse — so we built **realistic synthetic monthly data** with seasonality and trends."_ > **Show**: Time series plot + scatter (temp vs CO₂)

---

### Slide 3: Model & Results

> _"XGBoost with lagged features achieves **R² = 0.94**, MAE = 64 kt. It sees winter heating and energy trends clearly."_ > **Show**: Actual vs Predicted + Feature importance

---

### Slide 4: Live Demo (Streamlit)

> _"Let’s predict next 6 months! I’ll increase energy growth to 5%..."_ > **Run app live** → Show forecast rising → _"This triggers policy: shift load, add solar."_

---

### Slide 5: Ethics & Impact

> _"Open-source, adaptable, fair. Helps **any city** — even low-data ones. Enables **proactive decarbonization**."_ > **Show**: Streamlit + GitHub link

> _"Thank you! Code is on GitHub. Let's scale this to 100 cities."_

**Total: ~115 seconds + 3 min interactive demo**
