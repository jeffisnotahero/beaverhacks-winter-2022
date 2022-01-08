from flask import Flask
from flask_restful import Resource, Api

import requests

app = Flask(__name__)
api = Api(app)

def request_api_data():
    data = requests.get("https://api.covidactnow.org/v2/states.json?apiKey=")
    json = data.json()
    return json

def filter_actuals_data(json):
    actuals_data = {}
    for index, entry in enumerate(json):
            actuals_data[index] = {entry["state"]: 
            {"actuals": 
                {
                    "cases": entry["actuals"]["cases"],
                    "deaths": entry["actuals"]["deaths"],
                    "positiveTests": entry["actuals"]["positiveTests"],
                    "negativeTests": entry["actuals"]["negativeTests"],
                    "contactTracers": entry["actuals"]["contactTracers"],
                    "hospitalBedsCapacity": entry["actuals"]["hospitalBeds"]["capacity"],
                    "hospitalBedsCurrentUsageTotal": entry["actuals"]["hospitalBeds"]["currentUsageTotal"],
                    "hospitalBedsCurrentUsageCovid": entry["actuals"]["hospitalBeds"]["currentUsageCovid"],
                    "icuBedsCapacity": entry["actuals"]["icuBeds"]["capacity"],
                    "icuBedsCurrentUsageTotal": entry["actuals"]["icuBeds"]["currentUsageTotal"],
                    "icuBedsCurrentUsageCovid": entry["actuals"]["icuBeds"]["currentUsageCovid"],
                    "newCases": entry["actuals"]["newCases"],
                    "newDeaths": entry["actuals"]["newDeaths"],
                    "vaccinesDistributed": entry["actuals"]["vaccinesDistributed"],
                    "vaccinationsInitiated": entry["actuals"]["vaccinationsInitiated"],
                    "vaccinationsCompleted": entry["actuals"]["vaccinationsCompleted"],
                    "vaccinesAdministered": entry["actuals"]["vaccinesAdministered"],
                    "vaccinesAdministeredDemographics": entry["actuals"]["vaccinesAdministeredDemographics"],
                    "vaccinationsInitiatedDemographics": entry["actuals"]["vaccinationsInitiatedDemographics"]
                }}}
                
    return actuals_data

json = request_api_data()
actuals_data = filter_actuals_data(json)

class HelloWorld(Resource):
    def get(self):
        return actuals_data

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

# Environment variable
    # dotenv

# Call external API (Done)
    # request library

# Serialization (Done)
    # JSON

# Filter and organize data

    # Drop down list, state Dictionary (Greg)
        # State, JSON

    # General profile   (Greg)
        # State
            # Population
            # Risk level
            # Metrics
            # lastUpdatedDate

    # 2 Drop down list, Actuals (Jeff)
        # State
            # Actuals
                # Make HospitalBeds and icuBeds be list

# API End point Flask restful api

    # State selection   (Greg)

    # General profile   (Greg)

    # Actuals selection (Jeff)

# Deploy
    # Heroku