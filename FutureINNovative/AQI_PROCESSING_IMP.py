from API_FETCH_MAIN import *
from datetime import datetime

def safe_get(iaqi, key):
    return iaqi.get(key, {}).get("v", None)

def extract_pollutants(data):
    if not data:
        return {}

    iaqi = data["data"].get("iaqi", {})

    return {
        "city": data["data"]["city"].get("name"),
        "aqi": data["data"].get("aqi"),
        "pm25": safe_get(iaqi, "pm25"),
        "pm10": safe_get(iaqi, "pm10"),
        "no2": safe_get(iaqi, "no2"),
        "co": safe_get(iaqi, "co"),
        "o3": safe_get(iaqi, "o3"),
        "so2": safe_get(iaqi, "so2"),
        "temp": safe_get(iaqi, "t"),
        "hum": safe_get(iaqi, "h"),
        "pressure": safe_get(iaqi, "p"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# city_name = input("Enter city name: ")
# aqi_info = get_aqi_info(city_name)
# aqi_dict = extract_pollutants(aqi_info)
#
# print(aqi_dict)