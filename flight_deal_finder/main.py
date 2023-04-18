#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from pprint import pprint


#EDIT THE ROWS
API_GOOGLE_SHEET="https://api.sheety.co/99590fd56f514951e3e0791088f7aa9f/flightDeals/prices"

response=requests.get(API_GOOGLE_SHEET)
data=response.json()
pprint(data)











