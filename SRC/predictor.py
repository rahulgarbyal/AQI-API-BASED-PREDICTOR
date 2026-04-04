import pandas as pd
import joblib
import os
import numpy as np
from datetime import timedelta

def load_model():
    model_path = os.path.join("Models", "aqi_rf_model.pkl")
    model = joblib.load(model_path)
    return model

def load_data():
    data_path = os.path.join("DATA",
                             "processed",
                             "final_feature_dataset_aqi.csv"
                             )
    df = pd.read_csv(data_path)

    df['date'] = pd.to_datetime(
        df['date'],
        format='mixed',
        errors='coerce'
    )

    return df

def get_city_data(df, city_name):
    city_data = df[df['area'] == city_name]
    return city_data

def predict_latest_aqi(model, city_data):
    history = list(city_data['aqi_value'].values)

    dataset_latest_date = city_data["date"].max()
    today = pd.Timestamp.today()

    current_date = dataset_latest_date

    while current_date < today:
        next_date = current_date + timedelta(days=1)

        X_future = pd.DataFrame({
            "lag_1": [history[-1]],
            "lag_7": [history[-7]],
            "lag_30": [history[-30]],
            "rolling_7": [np.mean(history[-7:])],
            "rolling_30": [np.mean(history[-30:])],
            "month": [next_date.month],
            "day": [next_date.day],
            "day_of_week": [next_date.weekday()],
            "year": [next_date.year],
            "city_encoded": [city_data['city_encoded'].iloc[-1]],
            "state_encoded": [city_data['state_encoded'].iloc[-1]]
        })
        pred = model.predict(X_future)[0]

        history.append(pred)
        current_date = next_date

    tomorrow = today + timedelta(days=1)

    X_tomorrow = pd.DataFrame({
        "lag_1": [history[-1]],
        "lag_7": [history[-7]],
        "lag_30": [history[-30]],
        "rolling_7": [np.mean(history[-7:])],
        "rolling_30": [np.mean(history[-30:])],
        "month": [tomorrow.month],
        "day": [tomorrow.day],
        "day_of_week": [tomorrow.weekday()],
        "year": [tomorrow.year],
        "city_encoded": [city_data['city_encoded'].iloc[-1]],
        "state_encoded": [city_data['state_encoded'].iloc[-1]]
    })
    tomorrow_pred = model.predict(X_tomorrow)[0]

    return round(tomorrow_pred,2)

def predict_recent(model, city_data, days=7):
    history = list(city_data['aqi_value'].values)
    dataset_latest_date = city_data["date"].max()
    print(dataset_latest_date)
    today = pd.Timestamp.today()

    current_date = dataset_latest_date

    while current_date < today:
        next_date = current_date + timedelta(days=1)
        X_future = pd.DataFrame({
            "lag_1": [history[-1]],
            "lag_7": [history[-7]],
            "lag_30": [history[-30]],
            "rolling_7": [np.mean(history[-7:])],
            "rolling_30": [np.mean(history[-30:])],
            "month": [next_date.month],
            "day": [next_date.day],
            "day_of_week": [next_date.weekday()],
            "year": [next_date.year],
            "city_encoded": [city_data['city_encoded'].iloc[-1]],
            "state_encoded": [city_data['state_encoded'].iloc[-1]]
        })
        pred = model.predict(X_future)[0]
        history.append(pred)

        current_date = next_date

    predictions = []
    for i in range(days):
        future_date = today + timedelta(days=i+1)
        X_future_7 = pd.DataFrame({
            "lag_1": [history[-1]],
            "lag_7": [history[-7]],
            "lag_30": [history[-30]],
            "rolling_7": [np.mean(history[-7:])],
            "rolling_30": [np.mean(history[-30:])],
            "month": [future_date.month],
            "day": [future_date.day],
            "day_of_week": [future_date.weekday()],
            "year": [future_date.year],
            "city_encoded": [city_data['city_encoded'].iloc[-1]],
            "state_encoded": [city_data['state_encoded'].iloc[-1]]
        })

        next_7_pred = model.predict(X_future_7)[0]

        predictions.append({
            "date": future_date,
            "predicted_aqi": round(next_7_pred,2)
        })
        history.append(next_7_pred)

    return pd.DataFrame(predictions)

