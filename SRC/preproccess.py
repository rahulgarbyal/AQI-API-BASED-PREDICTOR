import pandas as pd


def load_data(file_path):

    #Load raw AQI dataset
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    #Clean AQI dataset
    # Drop useless column
    if 'note' in df.columns:
        df = df.drop(columns=['note'])

    # Convert date column
    df['date'] = pd.to_datetime(
        df['date'],
        format='mixed',
        dayfirst=True,
        errors='coerce'
    )

    # Remove invalid dates
    df = df.dropna(subset=['date'])

    # Clean text columns
    text_cols = [
        'state',
        'area',
        'prominent_pollutants',
        'air_quality_status',
        'unit'
    ]

    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].str.strip()

    # Sort by city and date
    df = df.sort_values(['area', 'date'])

    # Remove invalid AQI values
    df = df[df['aqi_value'] >= 0]

    return df


def save_cleaned_data(df, output_path):

   # Save cleaned dataset
    df.to_csv(output_path, index=False)


def preprocess_pipeline(input_path, output_path):
    #Complete preprocessing pipeline
    df = load_data(input_path)
    df = clean_data(df)
    save_cleaned_data(df, output_path)

    return df