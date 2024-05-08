from database.DB_connect import DBConnect
from modello.aereoporto import Aereoporto
from modello.voli import Volo
from modello.rotta import Rotta

class DAO():
    @staticmethod
    def getallflights(distanza):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.*
                FROM flights f 
                WHERE f.DISTANCE >%s """
        cursor.execute(query,(distanza,))

        for row in cursor:
            result.append(Volo(row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["Distanza"], row["TAIL_NUMBER"], row ["ORIGIN_AIRPORT_ID"],
                                     row["DESTINATION_AIRPORT_ID"],row["SCHEDULED_DEPARTURE_DATE"], row["DEPARTURE_DELAY"], row["ELAPSED_TIME"],
                               row["DISTANCE"],row["ARRIVAL_DATE"],row["ARRIVAL_DELAY"]))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT a.* FROM airports a "
        cursor.execute(query)

        for row in cursor:
            result.append(Aereoporto(row["ID"], row["IATA_CODE"], row["AIRPORT"], row["CITY"], row["STATE"],
                                     row["COUNTRY"], row["LATITUDE"], row["LONGITUDE"], row["TIMEZONE_OFFSET"]))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getRotte():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT 
    f.ORIGIN_AIRPORT_ID, 
    f.DESTINATION_AIRPORT_ID, 
    AVG(f.DISTANCE) AS Distanza
FROM 
    flights f
GROUP BY 
    f.ORIGIN_AIRPORT_ID, 
    f.DESTINATION_AIRPORT_ID;
"""
        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["Distanza"]))
        cursor.close()
        conn.close()
        return result





