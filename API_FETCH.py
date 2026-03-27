import requests
import requests as rq
from networkx.classes import non_neighbors

base_url = "https://api.waqi.info/feed/"
key = '3ca2567282608a5f5df1ca418243656c58d22465'
def get_aqi_info (city):
    url = f"{base_url}{city}/?token={key}"
    try:
        response = rq.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'ok':
                return data
            else:
                print("API returned error : ",data.get('data'))
                return None
        else:
            print(f"Failed to retrieve AQI data {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print("Request Failed : ",e)
        return None

city_name = input("Enter city name: ")
aqi_info = get_aqi_info(city_name)
if aqi_info and aqi_info['status'] == 'ok':
    print(f"{city_name} AQI is {aqi_info['data']['aqi']}")
    print(f"{city_name} Most dominant pollution is {aqi_info['data']['dominentpol']}")
else:
    print("Invalid city name or API error")