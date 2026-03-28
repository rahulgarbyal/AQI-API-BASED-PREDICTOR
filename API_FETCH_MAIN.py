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
