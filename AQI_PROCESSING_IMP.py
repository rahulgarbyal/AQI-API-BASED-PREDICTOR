from API_FETCH_MAIN import *

def extract_pollutants(data):
    iaqi = data["data"].get("iaqi", {})

    return {
        "aqi": data["data"].get("aqi"),
        "pm25": data["data"]["iaqi"]["pm25"]["v"],
        "pm10": data["data"]["iaqi"]["pm10"]["v"],
        "no2": data["data"]["iaqi"]["no2"]["v"],
        "co": data["data"]["iaqi"]["co"]["v"],
        "o3": data["data"]["iaqi"]["o3"]["v"],
        "so2": data["data"]["iaqi"]["so2"]["v"],
        "temp": data["data"]["iaqi"]["t"]["v"],
        "hum": data["data"]["iaqi"]["h"]["v"],
        "pressure": data["data"]["iaqi"]["p"]["v"]
    }

city_name = input("Enter city name: ")
aqi_info = get_aqi_info(city_name)
aqi_dict = extract_pollutants(aqi_info)

print(aqi_dict)