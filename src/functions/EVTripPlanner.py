from src.functions.TransactionManager import TransactionManager
from src.vendor.vehicleStatus import VehicleStatus
from src.vendor.maps import Maps


class EVTripPlanner:

    def planTrip(self, vin, source, destination):
        responce = {
            "transactionId": TransactionManager.initNewTransactionId(),
            "vin": vin,
            "source": source,
            "destination": destination,
            "distance": None,
            "currentChargeLevel": None,
            "errors": 'null'
        }

        # check battery status
        batteryStatus = VehicleStatus.getBatteryStatus(vin).json()
        if batteryStatus["error"] == None:
            responce["currentChargeLevel"] = batteryStatus["currentChargeLevel"]
            batteryStatus = responce["currentChargeLevel"]
        else:
            # if wrong vin return error 
            print("charge error")
            responce["errors"]=[{ "id": 9999, "description": "Technical Exception" }]
            return responce

        # get distance of trip
        distance = Maps.getDistance(source, destination).json()

        
        # Charging required or not
        if distance["error"] == None:
            responce["distance"] = distance["distance"]
            distance = responce["distance"]
        else:
            # if invalid source and destination, return error 
            print("invalid source destination")
            responce["errors"]=[{ "id": 9999, "description": "Technical Exception" }]
            return responce
        
        chargeReqiredToReachDestination = distance - batteryStatus
        # check if charge is required
        if (chargeReqiredToReachDestination > 0):
            responce["isChargingRequired"] = True
            optmalChargingLocations = Maps.getOptChargeStations(batteryStatus, distance, source, destination)
            if optmalChargingLocations == None:
                responce["errors"]=[{ "id": 9999, "description": "Technical Exception" }]
                print("error in charging stations")
                return responce
            elif len(optmalChargingLocations) == 0:
                responce["errors"]=[{ "id": 9999, "description":"Unable to reach the destination with the current charge level "}]
            else:
                responce["chargingStations"]=optmalChargingLocations
        else:
            responce["isChargingRequired"] = False


        return responce
