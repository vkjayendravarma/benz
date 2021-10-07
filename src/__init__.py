
from flask import Flask
from flask_api import status

app = Flask(__name__)

@app.route("/")
def index():
    return "Api working", status.HTTP_200_OK

from src.routes import getRoutePlan