
from src import app
from flask_api import status
from src.functions.EVTripPlanner import EVTripPlanner
from flask import request


@app.route('/getrouteplan', methods=['POST'])
def getrouteplan():
    routePlan = EVTripPlanner()
    query = request.get_json()
    res = routePlan.planTrip(query["vin"], query["source"], query["destination"])
    return res, status.HTTP_200_OK
