import requests

BASE_URL = "https://api.waqi.info/feed/"
API_KEY = "3ca2567282608a5f5df1ca418243656c58d22465"

def get_aqi_info(city):
    url = f"{BASE_URL}{city}/?token={API_KEY}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            if data.get("status") == "ok":
                return data
            else:
                print("API Error:", data.get("data"))
                return None
        else:
            print(f"HTTP Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print("Request Failed:", e)
        return None

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

if aqi_info:
    print(f"City Name: {city_name}")
    print(f"AQI: {aqi_info['data']['aqi']}")
else:
    print("No AQI data available")

aqi_dict = extract_pollutants(aqi_info)
print(aqi_dict)