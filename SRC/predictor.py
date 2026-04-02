import pandas as pd
import joblib

def load_model():
    model = joblib.load("../Models/aqi_rf_model.pkl")
    return model

def load_data():
    df = pd.read_csv("../DATA/processed/final_feature_dataset_aqi.csv")

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
    sample = city_data.iloc[-1]

    features = [
        'lag_1',
        'lag_7',
        'lag_30',
        'rolling_7',
        'rolling_30',
        'month',
        'day',
        'day_of_week',
        'year',
        'city_encoded',
        'state_encoded'
    ]

    X_sample = pd.DataFrame(
        [sample[features].values],
        columns=features
    )

    prediction = model.predict(X_sample)

    return prediction[0], sample['aqi_value']

def predict_recent(model, city_data):
    features = [
        'lag_1',
        'lag_7',
        'lag_30',
        'rolling_7',
        'rolling_30',
        'month',
        'day',
        'day_of_week',
        'year',
        'city_encoded',
        'state_encoded'
    ]

    recent = city_data.tail(20)

    X_recent = recent[features]
    y_actual = recent['aqi_value']

    y_pred = model.predict(X_recent)

    return recent, y_actual, y_pred