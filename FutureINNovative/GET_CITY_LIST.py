# from AQI_PROCESSING_IMP import extract_pollutants
# from API_FETCH_MAIN import get_aqi_info
# import requests
# import time
#
# city_list = ["Agra","Ahmedabad","Ajmer","Akola","Alappuzha","Aligarh","Alwar","Ambala","Amravati","Amritsar",
#     "Anand","Anantapur","Asansol","Aurangabad","Ayodhya","Azamgarh","Baddi","Baghpat","Balasore","Ballari",
#     "Banda","Bengaluru","Bankura","Baramati","Bareilly","Barmer","Bathinda","Beed","Begusarai","Belagavi",
#     "Berhampore","Berhampur","Bhagalpur","Bharatpur","Bharuch","Bhavnagar","Bhilai","Bhilwara","Bhiwadi","Bhiwandi",
#     "Bhopal","Bhubaneswar","Bhuj","Bidar","Bikaner","Bilaspur","Bokaro","Bulandshahr","Bundi","Chandigarh",
#     "Chandrapur","Chennai","Chhapra","Chhindwara","Chikkamagaluru","Chittoor","Coimbatore","Cuddalore","Cuttack","Darbhanga",
#     "Davanagere","Dehradun","Delhi","Deoghar","Dewas","Dhanbad","Dharwad","Dhule","Dibrugarh","Dindigul",
#     "Durg","Durgapur","Eluru","Erode","Etawah","Faridabad","Farrukhabad","Fatehpur","Firozabad","Gandhinagar",
#     "Gaya","Ghaziabad","Giridih","Gorakhpur","Greater Noida","Guntur","Gurugram","Guwahati","Gwalior",
#     "Haldia","Hapur","Haridwar","Hassan","Hazaribagh","Hisar","Hosur","Howrah","Hubballi","Hyderabad",
#     "Imphal","Indore","Jabalpur","Jaipur","Jalandhar","Jalgaon","Jammu","Jamnagar","Jamshedpur","Jhansi",
#     "Jhunjhunu","Jodhpur","Junagadh","Kakinada","Kalyan","Kannur","Kanpur","Karimnagar","Karnal","Karur",
#     "Kochi","Kohima","Kolhapur","Kolkata","Kollam","Kota","Kottayam","Kozhikode","Kurnool","Kurukshetra",
#     "Latur","Lucknow","Ludhiana","Madurai","Malda","Mangaluru","Mathura","Meerut","Mehsana",
#     "Moradabad","Motihari","Mumbai","Muzaffarnagar","Muzaffarpur","Mysuru","Nadiad","Nagaon","Nagpur","Nanded",
#     "Nashik","Navi Mumbai","Nellore","Noida","Ongole","Palakkad","Pali","Panipat","Parbhani","Patiala",
#     "Patna","Pilibhit","Pimpri-Chinchwad","Puducherry","Porbandar","Prayagraj","Pune","Raebareli","Raichur",
#     "Raipur","Rajahmundry","Rajkot","Rajnandgaon","Ramagundam","Rampur","Ranchi","Ratlam","Rewa","Rohtak",
#     "Rourkela","Sagar","Saharanpur","Salem","Sambalpur","Sangli","Satara","Satna","Shahjahanpur","Shillong",
#     "Shimla","Sikar","Siliguri","Sirsa","Solapur","Sonipat","Srinagar","Surat",
#     "Thane","Thanjavur","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tirupati","Tumakuru",
#     "Udaipur","Udupi","Ujjain","Unnao","Vadodara","Varanasi","Vellore","Vijayawada","Visakhapatnam","Warangal","Yamunanagar"
#     ]

# unknown = ['Akola', 'Alappuzha', 'Aligarh', 'Amravati', 'Anand', 'Ayodhya', 'Azamgarh', 'Balasore', 'Ballari', 'Banda',
#            'Bankura', 'Baramati', 'Barmer', 'Beed', 'Berhampore', 'Berhampur', 'Bharatpur', 'Bhavnagar', 'Bhilwara',
#            'Bhubaneswar', 'Bhuj', 'Bidar', 'Bikaner', 'Bokaro', 'Bundi', 'Chhindwara', 'Chittoor', 'Cuddalore', 'Cuttack',
#            'Davanagere', 'Deoghar', 'Dhanbad', 'Dharwad', 'Dhule', 'Dibrugarh', 'Eluru', 'Erode', 'Etawah', 'Farrukhabad',
#            'Fatehpur', 'Giridih', 'Guntur', 'Gurugram', 'Haridwar', 'Hazaribagh', 'Indore', 'Jalgaon', 'Jammu', 'Jamnagar',
#            'Jamshedpur', 'Jhunjhunu', 'Junagadh', 'Kakinada', 'Karimnagar', 'Karur', 'Kolhapur', 'Kottayam', 'Kurnool',
#            'Kurukshetra', 'Latur', 'Madurai', 'Malda', 'Mehsana', 'Mysuru', 'Nadiad', 'Nagaon', 'Nanded', 'Nellore',
#            'Ongole', 'Palakkad', 'Panipat', 'Parbhani', 'Pilibhit', 'Pimpri-Chinchwad', 'Porbandar', 'Prayagraj',
#            'Raebareli', 'Rajkot', 'Rajnandgaon', 'Ramagundam', 'Rampur', 'Ranchi', 'Rewa', 'Rourkela', 'Saharanpur',
#            'Sambalpur', 'Sangli', 'Satara', 'Shahjahanpur', 'Shimla', 'Sikar', 'Surat', 'Thanjavur', 'Tiruchirappalli',
#            'Tirunelveli', 'Tumakuru', 'Unnao', 'Vadodara', 'Vellore', 'Visakhapatnam', 'Warangal']

Known = ['Agra', 'Ahmedabad', 'Ajmer', 'Alwar', 'Ambala', 'Amritsar', 'Anantapur', 'Asansol', 'Aurangabad', 'Baddi',
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
# known2 = Known + known1
print(len(Known))
# print(known2)






































# BASE_URL = "https://api.waqi.info/feed/"
# API_KEY = "3ca2567282608a5f5df1ca418243656c58d22465"
#
# valid_cities = []
# invalid_cities = []
#
# for city in more_cities:
#     url = f"{BASE_URL}{city}/?token={API_KEY}"
#
#     try:
#         response = requests.get(url, timeout=5)
#         data = response.json()
#
#         if data.get("status") == "ok":
#             valid_cities.append(city)
#             print(f"✅ {city}")
#         else:
#             invalid_cities.append(city)
#             print(f"❌ {city} - {data.get('data')}")
#
#     except:
#         invalid_cities.append(city)
#         print(f"⚠️ {city} - request failed")
#
#     time.sleep(1)  # avoid rate limit
#
# print("\nVALID CITIES:\n", valid_cities)
# print("\nINVALID CITIES:\n", invalid_cities)