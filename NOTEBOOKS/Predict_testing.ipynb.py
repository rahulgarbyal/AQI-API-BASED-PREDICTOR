import pandas as pd
import joblib
import matplotlib.pyplot as plt

df = pd.read_csv("../DATA/processed/final_feature_dataset_aqi.csv")
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True, errors='coerce')

model = joblib.load("../Models/aqi_rf_model.pkl")

city_data = df[df['area'] == 'Delhi']
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

X_sample = pd.DataFrame([sample[features].to_dict()])

prediction = model.predict(X_sample)

print(f"PREDICTED AQI = {prediction[0]}")
print(f"ACTUAL AQI = {sample['aqi_value']}")

recent = city_data.tail(20)
X_recent = recent[features]
y_actual = recent['aqi_value']

y_pred = model.predict(X_recent)

plt.figure(figsize = (10,10))
plt.plot(recent['date'], y_actual, label = 'Actual')
plt.plot(recent['date'], y_pred, label = 'Predicted')
plt.legend()
plt.title('Actual vs Predicted Graph')
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.show()