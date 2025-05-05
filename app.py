import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="Smart Waste Tracker", page_icon="🍌", layout="centered")
st.title("🍌 Smart Waste Tracker")

# Simulated "live" detection
banana_weight = 0.18
banana_time = datetime.now().replace(microsecond=0)
detected_message = f"📡 {banana_weight:.2f} lbs of banana detected at {banana_time.strftime('%H:%M:%S')}"
st.subheader(detected_message)
st.divider()

# ---------------- MOCK LOG GENERATION ---------------- #
if "waste_log" not in st.session_state:
    food_items = [
        ("Apple", 0.22),
        ("Carrot", 0.10),
        ("Bread", 0.35),
        ("Avocado", 0.27),
        ("Yogurt Cup", 0.33),
        ("Lettuce", 0.19),
        ("Pizza Slice", 0.45),
        ("Tomato", 0.15),
        ("Orange Peel", 0.12)
    ]
    timestamps = [banana_time - timedelta(minutes=5 * i + random.randint(1, 4)) for i in range(len(food_items))]

    log_data = {
        "Timestamp": [t.strftime("%Y-%m-%d %H:%M:%S") for t in timestamps[::-1]] + [banana_time.strftime("%Y-%m-%d %H:%M:%S")],
        "Item": [item for item, _ in food_items[::-1]] + ["Banana"],
        "Weight (lbs)": [weight for _, weight in food_items[::-1]] + [banana_weight]
    }

    st.session_state.waste_log = pd.DataFrame(log_data)

# ---------------- DISPLAY LOG ---------------- #
st.subheader("🧾 Waste Log")
st.dataframe(st.session_state.waste_log, use_container_width=True)

# ---------------- DOWNLOAD BUTTON ---------------- #
csv = st.session_state.waste_log.to_csv(index=False)
st.download_button(
    label="📥 Download Waste Log as CSV",
    data=csv,
    file_name="waste_log.csv",
    mime="text/csv"
)
