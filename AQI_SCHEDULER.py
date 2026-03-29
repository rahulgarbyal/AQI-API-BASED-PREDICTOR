import time as tm
from datetime import time, timedelta, datetime
import schedule
from API_FETCH_MAIN import get_aqi_info
from AQI_PROCESSING_IMP import extract_pollutants
import pymongo

client = pymongo.MongoClient("mongodb+srv://RAHUL:Justx2006@aqicluster.1vdwpol.mongodb.net/")
db = client['AQI_DATABASE_TESTING']
collection = db['AQI_COLLECTION']

Known = ['Agra', 'Ahmedabad', 'Ajmer', 'Alwar']

def fetch_and_store_db():
    for city in Known:
        aqi_api_fetch_data = get_aqi_info(city)
        aqi_api_dict = extract_pollutants(aqi_api_fetch_data)
        collection.insert_one(aqi_api_dict)

schedule.every(30).seconds.do(fetch_and_store_db)

while True:
    schedule.run_pending()
    tm.sleep(1)




