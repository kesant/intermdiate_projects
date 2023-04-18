import requests
import os
from pprint import pprint

# list={"Paris":"PAR",
#     "Berlin":BER,
#     "Tokyo":,
#     "Sydney":,
#     "Istanbul":,
#     "Kuala Lumpur":,
#     "New York":,
#     "San Francisco":,
#     "Cape Town":""
#
#       }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass
    def get_data(self):
        API_GOOGLE_SHEET = "https://api.sheety.co/99590fd56f514951e3e0791088f7aa9f/flightDeals/prices"

        response = requests.get(API_GOOGLE_SHEET)
        data = response.json()['prices']
        return data
