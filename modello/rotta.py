from dataclasses import dataclass

@dataclass
class Rotta():
    ORIGIN_AIRPORT_ID:int
    DESTINATION_AIRPORT_ID:int
    Distanza:int

    def __hash__(self):
        return hash(self.ORIGIN_AIRPORT_ID+self.DESTINATION_AIRPORT_ID)

    def __str__(self):
        return f" ORIGIN_AIRPORT_ID: {self.ORIGIN_AIRPORT_ID} DESTINATION_AIRPORT_ID:{self.DESTINATION_AIRPORT_ID} Distanza: {self.Distanza}"