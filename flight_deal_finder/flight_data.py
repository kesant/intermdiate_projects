import requests
import os
from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime
from datetime import timedelta
#DEFINE THE PARAMETERS
CURRENCY="USD" #we define the currency
DATA_FLIGHTS=FlightSearch().data_sheet["prices"]#we get the data from the excel sheet
API_ENDPOINT="https://api.tequila.kiwi.com/v2/search"
START_CITY="LON"
DEPARTURE_CITY="London"
HEADERS={
    "apikey":os.environ["API_KEY_TEQUILA"]
}
#WE MODIFY THE DATES TO THE CORRECT FORMAT USING THE DATETIME LIBRARY

date_tomorrow=datetime.now().date()+timedelta(days=1)
date_come_back=date_tomorrow+timedelta(days=6*30)
date_tomorrow=date_tomorrow.strftime("%d/%m/%Y")
date_come_back=date_come_back.strftime("%d/%m/%Y")




class FlightData:
    #This class is responsible for structuring the flight data.
    pass
    def __init__(self):
        self.fly_from=""
        self.fly_to=""
        self.date_from=""
        self.date_to=""
        self.curr=""
        self.nights_in_dst_from=""
        self.nights_in_dst_to=""


        self.data=DATA_FLIGHTS
        self.price=""
        self.deperture_airport_code=START_CITY
        self.departure_city=DEPARTURE_CITY
        self.query={
            "fly_from":self.deperture_airport_code,
            "fly_to":"",
            "date_from":date_tomorrow,
            "date_to":date_come_back,
            "curr" : "USD",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,#with this parameter it return the cheapest flight
            "max_stopovers": 0
        }

    def get_info_flights(self):
        iata_codes=[code['iataCode'] for code in self.data]

        for codes in iata_codes:
            self.query["fly_to"] = codes
            response = requests.get(url=API_ENDPOINT, headers=HEADERS, params=self.query)
            response.raise_for_status()
            result=response.json()
            prices=result['data'][0]['price']
            pprint(f"{result['data'][0]['countryTo']['name']} : ${prices}")

flight=FlightData()
flight.get_info_flights()





