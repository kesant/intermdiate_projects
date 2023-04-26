import requests
from data_manager import DataManager
from pprint import pprint
import datetime
import os
from twilio.rest import Client


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,price,departure_city_name,departure_airport_IATA_code,arrival_city_name,arrival_airport_IATA_code,
                 outbound_data,inbound_data):
        self.price=price
        self.departure_city_name=departure_city_name
        self.departure_airport_IATA_code=departure_airport_IATA_code
        self.arrival_city_name=arrival_city_name
        self.arrival_airport_IATA_code=arrival_airport_IATA_code
        self.outbound_data=outbound_data
        self.inbound_data=inbound_data

    def send_notification(self):
        """this function will use the data from data manager and will compare
        the lowest price in the excel file with the price found in flight data to check if its lower
        if it does it sent a message  to the cell phone"""
        data=DataManager.get_data_manager()
        for indice in range(len(data['prices'])):
            lowestPrice=data['prices'][indice]['lowestPrice']
            city=data['prices'][indice]['city']
            iataCode=data['prices'][indice]['iataCode']
            if self.arrival_city_name==city:
                if self.price<=lowestPrice:
                        self.send_message()

    def send_message(self):
        """this function will send the message using the twilio API"""
        account_sid = "YOUR ACCOUNT_SID"
        auth_token = "YOURA AUTH TOKEN"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"lowest price alert! Only ${self.price} to fly from\n"
                 f"{self.departure_city_name}-{self.departure_airport_IATA_code} to {self.arrival_city_name}-{self.arrival_airport_IATA_code}\n"
                 f",from {self.inbound_data} to {self.outbound_data}" ,
            from_="+14066415511",
            to="+593987587609"
        )
        print("message sent succesfully")