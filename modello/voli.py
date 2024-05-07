from dataclasses import dataclass
from datetime import datetime
@dataclass
class Volo():
    ID:int
    AIRLINE_ID:int
    FLIGHT_NUMBER:int
    TAIL_NUMBER:str
    ORIGIN_AIRPORT_ID:int
    DESTINATION_AIRPORT_ID:int
    SCHEDULED_DEPARTURE_DATE:datetime
    DEPARTURE_DELAY:int
    ELAPSED_TIME:int
    DISTANCE:int
    ARRIVAL_DATE:datetime
    ARRIVAL_DELAY:datetime

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return (f"ID {self.ID} ")#Airline ID {self.AIRLINE_ID} FLIGHT_NUMBER {self.FLIGHT_NUMBER} ORIGIN_AIRPORT_ID {self.ORIGIN_AIRPORT_ID} DESTINATION_AIRPORT_ID {self.DESTINATION_AIRPORT_ID} DISTANCE {self.DISTANCE}")

    def __eq__(self, other):
        return self.ID==other.ID