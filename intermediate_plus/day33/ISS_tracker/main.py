import requests
from datetime import datetime

MY_LAT = 61.314152 # Your latitude
MY_LONG = 23.752541 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise, sunset)

time_now = datetime.now()
current_hour = time_now.hour
print(current_hour)

if iss_latitude >= 56.0 and iss_latitude <= 66.0 and iss_longitude >= 13.0 and iss_longitude <= 33.0:
    if current_hour < sunrise or current_hour > sunset:
        print("ISS is visible.")
else:
    print("ISS is not visible at the moment.")

#Skipped the email part here. 



