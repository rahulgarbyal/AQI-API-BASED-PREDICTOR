from API_FETCH_MAIN import get_aqi_info
from AQI_PROCESSING_IMP import extract_pollutants
import pymongo

client = pymongo.MongoClient("mongodb+srv://RAHUL:Justx2006@aqicluster.1vdwpol.mongodb.net/")
db = client['AQI_DATABASE_ORIGINAL']
collection = db['AQI_COLLECTION_ORIGINAL']

Known = ['Agra', 'Ahmedabad', 'Ajmer', 'Alwar','Ambala', 'Amritsar', 'Anantapur', 'Asansol', 'Aurangabad', 'Baddi',
         'Baghpat', 'Bengaluru', 'Bareilly', 'Bathinda', 'Begusarai', 'Belagavi', 'Bhagalpur', 'Bharuch', 'Bhilai',
         'Bhiwadi', 'Bhiwandi', 'Bhopal', 'Bilaspur', 'Bulandshahr', 'Chandigarh', 'Chandrapur', 'Chennai', 'Chhapra',
         'Chikkamagaluru', 'Coimbatore', 'Darbhanga', 'Dehradun', 'Delhi', 'Dewas', 'Dindigul', 'Durg', 'Durgapur',
         'Faridabad', 'Firozabad', 'Gandhinagar', 'Gaya', 'Ghaziabad', 'Gorakhpur', 'Greater Noida', 'Guwahati',
         'Gwalior', 'Haldia', 'Hapur', 'Hassan', 'Hisar', 'Hosur', 'Howrah', 'Hubballi', 'Hyderabad', 'Imphal', 'Jabalpur',
         'Jaipur', 'Jalandhar', 'Jhansi', 'Jodhpur', 'Kalyan', 'Kannur', 'Kanpur', 'Karnal', 'Kochi', 'Kohima', 'Kolkata',
         'Kollam', 'Kota', 'Kozhikode', 'Lucknow', 'Ludhiana', 'Mangaluru', 'Mathura', 'Meerut', 'Moradabad', 'Motihari',
         'Mumbai', 'Muzaffarnagar', 'Muzaffarpur', 'Nagpur', 'Nashik', 'Navi Mumbai', 'Noida', 'Pali', 'Patiala', 'Patna',
         'Puducherry', 'Pune', 'Raichur', 'Raipur', 'Rajahmundry', 'Ratlam', 'Rohtak', 'Sagar', 'Salem', 'Satna',
         'Shillong', 'Siliguri', 'Sirsa', 'Solapur', 'Sonipat', 'Srinagar', 'Thane', 'Thiruvananthapuram', 'Thrissur',
         'Tirupati', 'Udaipur', 'Udupi', 'Ujjain', 'Varanasi', 'Vijayawada', 'Yamunanagar', 'Aizawl', 'Agartala',
         'Itanagar', 'Gangtok', 'Daman', 'Silvassa', 'Leh','Bhiwani', 'Kaithal', 'Charkhi Dadri', 'Palwal',
         'Fatehabad', 'Jind', 'Araria', 'Katihar', 'Siwan', 'Buxar', 'Chapra', 'Damoh', 'Jeypore', 'Yadgir','Bagalkot',
         'Koppal', 'Haveri', 'Gadag', 'Ramanathapuram', 'Thoothukudi','Ankleshwar', 'Churu','Saharsa', 'Kishanganj', 'Mon']

def fetch_and_store_db():
    for city in Known:
        aqi_api_fetch_data = get_aqi_info(city)

        if not aqi_api_fetch_data:
            continue

        aqi_api_dict = extract_pollutants(aqi_api_fetch_data)
        collection.insert_one(aqi_api_dict)

if __name__ == "__main__":
    fetch_and_store_db()




