import requests as rq

def get_coords(city):
    url = f"https://nominatim.openstreetmap.org/search"

    parameters = {
        "q": city,
        "format": "json",
        "addressdetails": 1,
        "limit": 1
    }

    headers = {
        "User-Agent": "aqi-app"
    }

    response = rq.get(url, params=parameters, headers=headers, timeout=5)
    data = response.json()

    if data:
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return lat, lon
    else:
        return None ,None

def get_bounds_coords(lat, lon, offset=1.0):
    lat_min = lat - offset
    lat_max = lat + offset
    lon_min = lon - offset
    lon_max = lon + offset

    return f"{lat_min},{lon_min},{lat_max},{lon_max}"

city = "delhi"
lat, lon = get_coords(city)
bounds = get_bounds_coords(lat, lon)

print(bounds)