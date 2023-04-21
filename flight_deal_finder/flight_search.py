import requests
import main
from pprint import pprint
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __int__(self):
        self.data_sheet=main.sheet_data
    def update_dat(self):
        self.data_sheet=main.sheet_data
        for indice in range(len(self.data_sheet['prices'])):
            if len(self.data_sheet['prices'][indice]['iataCode'])==0:
                self.data_sheet['prices'][indice]['iataCode']="TESTING"
        pprint(self.data_sheet)
#################################
flight_data=FlightSearch()
pprint(flight_data.data_sheet)