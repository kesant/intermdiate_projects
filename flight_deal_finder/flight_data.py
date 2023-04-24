import requests
import os
from pprint import pprint
from flight_search import FlightSearch

CURRENCY="USD"
DATA_FLIGHTS=FlightSearch().data_sheet

class FlightData:
    #This class is responsible for structuring the flight data.
    pass
    def __init__(self):
        self.data=DATA_FLIGHTS
flight=FlightData()
print(flight.data)