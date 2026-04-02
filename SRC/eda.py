import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def load_data():
    df = pd.read_csv("../DATA/processed/cleaned_aqi.csv")
    df['date'] = pd.to_datetime(
        df['date'],
        format='mixed',
        errors='coerce'
    )
    return df

def aqi_distribution(df):
    plt.figure(figsize=(10, 5))
    plt.hist(df['aqi_value'], bins=50)
    plt.title("Distribution of AQI Values")
    plt.xlabel("AQI")
    plt.ylabel("Frequency")
    st.pyplot(plt)

def top_polluted_cities(df):
    top_cities = df.groupby('area')['aqi_value'].mean() \
                   .sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 5))
    top_cities.plot(kind='bar')
    plt.title("Top 10 Most Polluted Cities")
    plt.ylabel("Average AQI")
    st.pyplot(plt)

def top_clean_cities(df):
    clean_cities = df.groupby('area')['aqi_value'].mean() \
                     .sort_values().head(10)

    plt.figure(figsize=(10, 5))
    clean_cities.plot(kind='bar')
    plt.title("Top 10 Clean Cities")
    plt.ylabel("Average AQI")
    st.pyplot(plt)

def monthly_trend(df):
    df['month'] = df['date'].dt.month

    monthly = df.groupby('month')['aqi_value'].mean()

    plt.figure(figsize=(10, 5))
    monthly.plot(marker='o')
    plt.title("Monthly AQI Trend")
    plt.xlabel("Month")
    plt.ylabel("Average AQI")
    plt.grid(True)
    st.pyplot(plt)

def yearly_trend(df):
    df['year'] = df['date'].dt.year

    yearly = df.groupby('year')['aqi_value'].mean()

    plt.figure(figsize=(10, 5))
    yearly.plot(marker='o')
    plt.title("Yearly AQI Trend")
    plt.xlabel("Year")
    plt.ylabel("Average AQI")
    plt.grid(True)
    st.pyplot(plt)

def city_trend(df, city_name):
    city_data = df[df['area'] == city_name]
    plt.figure(figsize=(10, 5))
    plt.plot(city_data['date'], city_data['aqi_value'])
    plt.title(f"{city_name} Historical AQI Trend")
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.xticks(rotation=45)
    st.pyplot(plt)
