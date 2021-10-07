import requests
from config import Config
import json

class VehicleStatus:
    @staticmethod
    def getBatteryStatus(vin):
        response = requests.post(Config.DATA_API + "charge_level" ,data=json.dumps({ "vin": vin }),headers={"Content-Type":"application/json"})
        return response