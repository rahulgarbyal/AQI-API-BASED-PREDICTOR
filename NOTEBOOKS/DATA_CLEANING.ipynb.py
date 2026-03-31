import pandas as pd
df = pd.read_csv("../DATA/raw/aqi.csv")
df.head()
df.isnull().sum()
df = df.drop(columns=['note'])

df['date'] = pd.to_datetime(df['date'],dayfirst=True)
df.info()
# print(df.duplicated().sum())

text_cols = ['state', 'area', 'prominent_pollutants',
             'air_quality_status', 'unit']

for col in text_cols:
    df[col] = df[col].str.strip()

df = df.sort_values(['area', 'date'])

# print(df['aqi_value'].describe())

df = df[df['aqi_value'] >= 0]
print(df['area'].nunique())

df.to_csv("../DATA/processed/cleaned_aqi.csv", index=False)
