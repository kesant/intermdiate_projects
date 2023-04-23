import requests
import main
from pprint import pprint
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.data_sheet=main.sheet_data

    def update_iataCode(self):
        self.data_sheet=main.sheet_data
        for indice in range(len(self.data_sheet['prices'])):
            if len(self.data_sheet['prices'][indice]['iataCode'])!=0:
                self.data_sheet['prices'][indice]['iataCode']=""
#################################

flight_data=FlightSearch()
flight_data.update_iataCode()
pprint(flight_data.data_sheet)
