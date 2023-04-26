import requests
import os
from pprint import pprint

#DEFINE THE PARAMETERS
API_ENDPOINT="https://api.tequila.kiwi.com/v2/search"




class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,fly_from,fly_to,date_from,date_to,curr,nights_in_dst_from,nights_in_dst_to,
                 flight_type,one_for_city,max_stopovers):
        self.fly_from=fly_from
        self.fly_to=fly_to
        self.date_from=date_from
        self.date_to=date_to
        self.curr=curr
        self.nights_in_dst_from=nights_in_dst_from
        self.nights_in_dst_to=nights_in_dst_to
        self.flight_type=flight_type
        self.one_for_city=one_for_city
        self.max_stopovers=max_stopovers



    def get_info_flights(self):
        headers = {
            "apikey": os.environ["API_KEY_TEQUILA"]
        }
        query = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": self.curr,
            "nights_in_dst_from": self.nights_in_dst_from,
            "nights_in_dst_to": self.nights_in_dst_to,
            "flight_type": self.flight_type,
            "one_for_city": self.one_for_city,  # with this parameter it return the cheapest flight
            "max_stopovers": self.max_stopovers
        }

        response = requests.get(url=API_ENDPOINT, headers=headers, params=query)
        response.raise_for_status()
        result=response.json()
        prices=result['data'][0]['price']
        pprint(f"{result['data'][0]['countryTo']['name']} : ${prices}")





