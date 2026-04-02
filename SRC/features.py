import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_cleaned_data(file_path):

    # Load cleaned AQI dataset

    df = pd.read_csv(file_path)

    df['date'] = pd.to_datetime(
        df['date'],
        format='mixed',
        dayfirst=True,
        errors='coerce'
    )

    return df

def create_lag_features(df):
    #Create lag-based AQI features

    df = df.sort_values(['area', 'date'])
    df['lag_1'] = df.groupby('area')['aqi_value'].shift(1)
    df['lag_7'] = df.groupby('area')['aqi_value'].shift(7)
    df['lag_30'] = df.groupby('area')['aqi_value'].shift(30)
    return df

def create_rolling_features(df):
    # Create rolling average features
    df['rolling_7'] = df.groupby('area')['aqi_value'].transform(lambda x: x.rolling(7).mean())
    df['rolling_30'] = df.groupby('area')['aqi_value'].transform(lambda x: x.rolling(30).mean())
    return df

def create_date_features(df):

    # Create date-based features
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_week'] = df['date'].dt.dayofweek
    df['year'] = df['date'].dt.year

    return df


def encode_features(df):
    # Encode city and state columns

    le_city = LabelEncoder()
    df['city_encoded'] = le_city.fit_transform(df['area'])

    le_state = LabelEncoder()
    df['state_encoded'] = le_state.fit_transform(df['state'])

    return df, le_city, le_state


def feature_pipeline(input_path, output_path):

    # Complete feature engineering pipeline

    df = load_cleaned_data(input_path)

    df = create_lag_features(df)
    df = create_rolling_features(df)
    df = create_date_features(df)

    df, le_city, le_state = encode_features(df)

    df = df.dropna()  #or df.dropna(inplace = True)

    df.to_csv(output_path, index=False)

    return df, le_city, le_state