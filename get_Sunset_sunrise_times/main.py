import requests
from datetime import datetime

MY_LAT=51.587351
MY_LNG=-9.127758
#we create a python dictionary for the parameters we are gonna sen to the request
parameters={"lat":MY_LAT,"lng":MY_LNG,"formatted":0}#formatted gives us the time in 24 hours format


response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)
time_now=datetime.now().hour
print(time_now)