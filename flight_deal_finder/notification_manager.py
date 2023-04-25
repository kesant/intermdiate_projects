import requests

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
