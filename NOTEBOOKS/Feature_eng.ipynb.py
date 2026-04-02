import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../DATA/processed/cleaned_aqi.csv")
df['date'] = pd.to_datetime(df['date'], format = 'mixed', dayfirst=True, errors='coerce')

#if any row is invalid, instead of crashing it becomes = Not a Time
#then remove it safely

df = df.sort_values(['area', 'date'])
df.head()

#lag features
df['lag_1'] = df.groupby('area')['aqi_value'].shift(1)
df['lag_7'] = df.groupby('area')['aqi_value'].shift(7)
df['lag_30'] = df.groupby('area')['aqi_value'].shift(30)

#rolling avgs

df['rolling_7'] = df.groupby('area')['aqi_value'].transform(lambda x: x.rolling(7).mean())
df['rolling_30'] = df.groupby('area')['aqi_value'].transform(lambda x: x.rolling(30).mean())

#date based
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_of_week'] = df['date'].dt.dayofweek
df['year'] = df['date'].dt.year

le_city = LabelEncoder()
df['city_encoded'] = le_city.fit_transform(df['area'])

le_state = LabelEncoder()
df['state_encoded'] = le_state.fit_transform(df['state'])

df.dropna()

df.to_csv("../DATA/processed/final_feature_dataset_aqi.csv")


