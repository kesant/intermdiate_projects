import requests
from pprint import pprint
import os
from datetime import datetime
from datetime import timedelta

from flight_data import FlightData

#VARIABLES



START_CITY="LON"
DEPARTURE_CITY="London"
API_ENDPOINT="https://api.tequila.kiwi.com"
NIGHTS_IN_DST_FROM=7
CURR= "USD"
NIGHTS_IN_DST_TO= 28
FLIGHT_TYPE= "round"
ONE_FOR_CITY= 1  # with this parameter it return the cheapest flight
MAX_STOPOVERS= 0


#CLASS
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def update_iataCode(self,data_sheet):
        """if the iata code in the data given is empty it will searh the iata
        code and put it in the parameter iata code"""

        prices=data_sheet['prices']#we save  the lists of  data form the sheet prices

        for indice in range(len(prices)):

            iata_code=data_sheet['prices'][indice]['iataCode']#we save every iata code in the iteration
            city=data_sheet['prices'][indice]['city']#we save the city in every iteration

            if len(iata_code)==0:

                data_sheet['prices'][indice]['iataCode']=self.get_iata_code(city)
        return data_sheet

    def get_iata_code(self,city):
        """get the iata code using the tequila api  and the city"""

        API_ENDPOINT_TEQUILA = f"{API_ENDPOINT}/locations/query"
        params={
            "term":city,
            "location_types": "city"
        }
        headers = {
            "apikey": os.environ["API_KEY_TEQUILA"]
        }
        response=requests.get(url=API_ENDPOINT_TEQUILA,headers=headers,params=params)
        response.raise_for_status()
        code_iata=response.json()["locations"][0]["code"]
        return code_iata

    def get_flight_data(self,data_sheet):
        """Get the list of lowest prices"""
        price_fligts=[]
        #we get the dates
        date_tomorrow = datetime.now().date() + timedelta(days=1)
        date_come_back = date_tomorrow + timedelta(days=6 * 30)
        date_tomorrow = date_tomorrow.strftime("%d/%m/%Y")
        date_come_back = date_come_back.strftime("%d/%m/%Y")


        iata_codes=[code['iataCode'] for code in data_sheet['prices']]

        for codes in iata_codes:
            information_flight=FlightData(START_CITY,codes,date_tomorrow,date_come_back,CURR,NIGHTS_IN_DST_FROM,NIGHTS_IN_DST_TO,
                     FLIGHT_TYPE,ONE_FOR_CITY,MAX_STOPOVERS)
            price_fligts.append(information_flight.get_info_flights())
        return price_fligts
    def send_notifications(self):
        pass
#################################

