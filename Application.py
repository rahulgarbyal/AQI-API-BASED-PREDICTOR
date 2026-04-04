import streamlit as st
import pandas as pd
from SRC.predictor import load_model, get_city_data, predict_latest_aqi, load_data,predict_recent
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
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Predict Tomorrow AQI"):
        tomorrow_pred = predict_latest_aqi(model, city_data)

        st.subheader(f"Tomorrow AQI for - {city}")
        st.metric("Predicted AQI", round(tomorrow_pred, 2))

        st.write("### **AQI STATUS**")
        status = get_aqi_status(tomorrow_pred)
        st.write(status)
with col2:
    if st.button("Predict 7 days AQI"):
        future_pred = predict_recent(model, city_data, 7)
        st.subheader(f"Next 7 days AQI for - {city}")

        st.dataframe(future_pred)

        st.line_chart(future_pred.set_index('date')['predicted_aqi'])

#Historical graph
st.subheader(f"AQI Trends for {city}")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write("### **LATEST RECORDED**")
    recent = city_data.tail(30)

    plt.figure(figsize=(5, 4))
    plt.plot(recent['date'], recent['aqi_value'],marker='o')
    plt.title(f"Last 30 days AQI Trend of Latest Recorded Data of - {city}")
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.xticks(rotation=45)
    plt.grid(True)

    st.pyplot(plt)

with col2:
    st.write("### Monthly AQI Trend")
    monthly = city_data.groupby('month')['aqi_value'].mean()

    plt.figure(figsize=(5, 4))
    plt.plot(monthly.index, monthly.values)
    plt.title(f"Monthly AQI Trend for {city}")
    plt.xlabel("Month")
    plt.ylabel("AQI")
    plt.grid(True)
    st.pyplot(plt)

with col3:
    st.write("### Historical AQI Trend")
    city_trend(df, city)
