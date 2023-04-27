#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from pprint import pprint
from data_manager import DataManager
from flight_data import  FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


#EDIT THE ROWS
#pprint(sheet_data)#print the data in a better way
####WE GET THE DATA##########

DataManager.update_sheet()#we update the sheet with the IATA codes in case it doesn't have it
initial_data=DataManager.get_data_manager()#we get the data
price_flights_list=FlightSearch.get_flight_data(initial_data)#we get the list of the cheapest price flights for every destination
FlightSearch.send_notifications(price_flights_list)#we get the flights list of prices and send the notification to the phone in case its cheaper than the price in the excel sheet
















