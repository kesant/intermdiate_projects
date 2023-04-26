import requests
import os
from pprint import pprint
from flight_search import FlightSearch

API_GOOGLE_SHEET="https://api.sheety.co/99590fd56f514951e3e0791088f7aa9f/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_data_manager(self):
        response = requests.get(API_GOOGLE_SHEET)
        sheet_data = response.json()
        return sheet_data

    def update_sheet(self):
        """update the information in the excel sheet using the sheety API """
        data=self.get_data_manager()
        updated_data=FlightSearch().update_iataCode(data)
        for indice in range(len(updated_data['prices'])):
             id_column=updated_data['prices'][indice]['id']
             API_GOOGLE_SHEET_ENDPOINT= f"{API_GOOGLE_SHEET}/{id_column}"
             body={"price":{
                 'city': updated_data['prices'][indice]['city'],
                 'iataCode': updated_data['prices'][indice]['iataCode'],
                 'lowestPrice': updated_data['prices'][indice]['lowestPrice']
             }}
             reponse=requests.put(url=API_GOOGLE_SHEET_ENDPOINT,json=body)
             reponse.raise_for_status()

manager=DataManager().get_data_manager()
pprint(manager)
flighst_price=FlightSearch()
flighst_price.get_flight_data(manager)
