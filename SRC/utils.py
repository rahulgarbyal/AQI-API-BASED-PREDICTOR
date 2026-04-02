FEATURES = [
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


def get_aqi_status(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"