# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import  requests


api_key=""
parameters={
    "lat":-2.170998,
    "lon":-79.922356,
    "appid":api_key
}
response=requests.get("https://pro.openweathermap.org/data/2.5/forecast/hourly",params=parameters)
print(response.status_code)
response.raise_for_status()
data=response.json()["Hourly"][:12]
will_rain=False
for hour_data in data:
    condition=hour_data["weather"][0]["id"]
    if int(condition)<700:
        will_rain=True
if will_rain:
    print("Bring an umbrella")
print(data)