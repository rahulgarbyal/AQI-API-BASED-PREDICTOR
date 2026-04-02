import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

df = pd.read_csv("../DATA/processed/final_feature_dataset_aqi.csv")
df.head()

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

X = df[features]
y = df['aqi_value']


#train-test-split
split_index = int(len(df) * 0.8)  #80% training and 20% testing

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

model = RandomForestRegressor(n_estimators=50,
                              max_depth=15,
                              random_state=42,
                              n_jobs=-1
                              )

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("MAE: ", mae)
print("RMSE: ", rmse)
print("R2: ", r2)

joblib.dump(model, "../Models/aqi_rf_model.pkl")
print("Model saved successfully!")