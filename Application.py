import streamlit as st
import pandas as pd
from SRC.predictor import load_model, load_model, get_city_data, predict_latest_aqi, load_data
from SRC.eda import city_trend
from SRC.utils import get_aqi_status
import matplotlib.pyplot as plt

st.set_page_config(page_title="AQI FORECAST DASHBOARD", layout="wide")
st.title("AQI FORECASTING DASHBOARD")
st.write("Predict next-day aqi based on historical data")

model = load_model()
df = load_data()

st.sidebar.title("Select City")
city = st.sidebar.selectbox("Choose City",
                            sorted(df["area"].unique())
)

city_data = get_city_data(df, city)
predicted_aqi, actual_aqi = predict_latest_aqi(model, city_data)

status = get_aqi_status(predicted_aqi)

col1,col2,col3 = st.columns(3)
with col1:
    st.metric("Predicted AQI", round(predicted_aqi,2))

with col2:
    st.metric("Last Actual AQI", round(actual_aqi,2))

with col3:
    st.metric("Air Quality Status", status)

#Historical graph
st.subheader(f"AQI Trend for {city}")
col1, col2 = st.columns(2)

with col1:
    st.write("### Historical AQI Trend")

    recent = city_data.tail(30)

    plt.figure(figsize=(5, 4))
    plt.plot(recent['date'], recent['aqi_value'])
    plt.title(f"Last 30 days AQI Trend of Latest Recorded Data of - {city}")
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.xticks(rotation=45)
    plt.grid(True)

    st.pyplot(plt)

with col2:
    st.write("### Monthly AQI Trend")

    monthly = city_data.groupby('month')['aqi_value'].mean()

    st.line_chart(monthly)
