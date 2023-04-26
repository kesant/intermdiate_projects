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
API_GOOGLE_SHEET="https://api.sheety.co/99590fd56f514951e3e0791088f7aa9f/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_data_manager(self):
        response = requests.get(API_GOOGLE_SHEET)
        sheet_data = response.json()
        return sheet_data
    # def update_sheet(self):
    #
    #     flight_data=FlightSearch()
    #     flight_data.update_iataCode()
    #
    #     for indice in range(len(flight_data.data_sheet['prices'])):
    #          id_column=flight_data.data_sheet['prices'][indice]['id']
    #          API_GOOGLE_SHEET_ENDPOINT= f"{API_GOOGLE_SHEET}/{id_column}"
    #          body={"price":{
    #              'city': flight_data.data_sheet['prices'][indice]['city'],
    #              'iataCode': flight_data.data_sheet['prices'][indice]['iataCode'],
    #              'lowestPrice': flight_data.data_sheet['prices'][indice]['lowestPrice']
    #          }}
    #          pprint(body)
    #          reponse=requests.put(url=API_GOOGLE_SHEET,json=body)
    #          reponse.raise_for_status()

