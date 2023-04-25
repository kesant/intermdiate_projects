import requests
import main
from pprint import pprint
import os
from datetime import datetime
from datetime import timedelta
#VARIABLES


date_tomorrow=datetime.now().date()+timedelta(days=1)
date_come_back=date_tomorrow+timedelta(days=6*30)
date_tomorrow=date_tomorrow.strftime("%d/%m/%Y")
date_come_back=date_come_back.strftime("%d/%m/%Y")
START_CITY="LON"
DEPARTURE_CITY="London"
API_ENDPOINT="https://api.tequila.kiwi.com"



#CLASS
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.data_sheet=main.sheet_data
        self.API_ENDPOINT_TEQUILA="https://api.tequila.kiwi.com/locations/query"
        self.headers={
            "apikey":os.environ["API_KEY_TEQUILA"]
        }
        self.params={
            "term":"",
            "location_types": "city"
        }
    def update_iataCode(self):

        for indice in range(len(self.data_sheet['prices'])):
            if len(self.data_sheet['prices'][indice]['iataCode'])==0:
                self.params["term"] = self.data_sheet['prices'][indice]['city']
                self.data_sheet['prices'][indice]['iataCode']=self.get_iata_code(self.params["term"] )
        pprint(self.data_sheet)

    def get_iata_code(self,city):
        """get the iata code using the tequila api  and the city"""
        self.params["term"] =city
        print(self.params)
        response=requests.get(url=self.API_ENDPOINT,headers=self.headers,params=self.params)
        response.raise_for_status()
        code_iata=response.json()["locations"][0]["code"]
        return code_iata
    def get_flight_data(self):
        HEADERS = {
            "apikey": os.environ["API_KEY_TEQUILA"]
        }

        pass

#################################

flight_data=FlightSearch()
flight_data.update_iataCode()

