from flask import Flask
from flask_restful import Resource, Api

import requests

app = Flask(__name__)
api = Api(app)

data = requests.get("https://api.covidactnow.org/v2/states.json?apiKey=")
json = data.json()

class HelloWorld(Resource):
    def get(self):
        return json

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