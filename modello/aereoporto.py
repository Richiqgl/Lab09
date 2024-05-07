from dataclasses import dataclass

@dataclass
class Aereoporto():
    ID:int
    IATA_CODE:str
    AIRPORT:str
    CITY:str
    STATE:str
    COUNTRY:str
    LATITUDE:int
    LONGITUDE:int
    TIMEZONE_OFFSET:int

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"ID: {self.ID} IATA_CODE: {self.IATA_CODE} NOME AEREOPORTO: {self.AIRPORT} STATE: {self.STATE} PAESE: {self.COUNTRY}"

    def __eq__(self, other):
        return self.ID==other.ID