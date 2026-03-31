import requests as rq
from Coordinates import *

base_url = "https://api.waqi.info/feed/map/bounds/"
key = '3ca2567282608a5f5df1ca418243656c58d22465'

def extract_aqi_s(stations):
    aqi_list = []
    for station in stations:
        aqi = station.get("aqi")
        if isinstance(aqi, int):
            aqi_list.append(aqi)
    return aqi_list

def calculate_aqi(aqi_list):
    if not aqi_list:
        return None, None
    avg_aqi = sum(aqi_list)/len(aqi_list)
    max_aqi = max(aqi_list)

    return avg_aqi, max_aqi

def get_all_stations_aqi_info (city_name):
    lat, lon = get_coords(city_name)
    if lat is None or lon is None:
        print("Invalid city name or API error")
        return []

    bounds = get_bounds_coords(lat, lon)
    url = f"{base_url}?latlng={bounds}&token={key}"
    try:
        response = rq.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            if data['status'] == 'ok':
                return data["data"]
            else:
                print("API returned error : ",data.get('data'))
                return []
        else:
            print(f"Failed to retrieve AQI data {response.status_code}")
            return []
    except rq.exceptions.RequestException as e:
        print("Request Failed : ",e)
        return []

#comment out later
city_name = input("Enter city name: ")
stations = get_all_stations_aqi_info(city_name)
aqi_values= extract_aqi_s(stations)
avg_aqi, max_aqi = calculate_aqi(aqi_values)

print(f"{city_name}'s AQI is {avg_aqi}")
print(f"{city_name}'s max AQI is {max_aqi}")