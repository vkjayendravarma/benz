import requests
from config import Config
import json


class Maps:
    @staticmethod
    def getDistance(source, destination):
        response = requests.post(Config.DATA_API + "distance", data=json.dumps({
            "source": source,
            "destination": destination
        }), headers={"Content-Type": "application/json"})
        return response

    @staticmethod
    def getOptChargeStations(batteryRange, distance, source, destination):
        result = []
        currentBatteryRange = batteryRange
        
        # get all charging stations in the path
        response = requests.post(Config.DATA_API + "charging_stations", data=json.dumps({
            "source": source,
            "destination": destination
        }), headers={"Content-Type": "application/json"}).json()

        chargingStations = []

        if response["error"] == None:
            chargingStations = response["chargingStations"]
        else:
            # return techincal error 
            return None
      
        pitStops = sorted(chargingStations,key=lambda k: k['limit'], reverse=True)
        while batteryRange < distance:
            numberOfPitsStopsLeft = len(pitStops)
            refill = 0
            for stop in range(numberOfPitsStopsLeft):
                # can I reach this
                if pitStops[stop]["distance"] <= currentBatteryRange:
                    currentBatteryRange = currentBatteryRange - pitStops[stop]["distance"] + pitStops[stop]["limit"]
                    if(currentBatteryRange>100):
                        currentBatteryRange = 100
                    batteryRange = batteryRange + pitStops[stop]["limit"]
                    result.append(pitStops[stop])
                    del pitStops[stop]
                    refill = 1
                    break
            if refill == 0:
                # if there is no refill then destination can't be reached 
                return []
            
        
        return sorted(result,key=lambda k: k['distance'])
