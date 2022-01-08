from dotenv.main import dotenv_values
from flask import Flask
from flask_restful import Resource, Api, abort

from helper import request_api_data, filter_actuals_data

app = Flask(__name__)
api = Api(app)

json = request_api_data()
actuals_data = filter_actuals_data(json)

class Homepage(Resource):
    """
    API endpoint for homepage.
    """
    def get(self):
        """
        GET method.
        """
        return {'hello': 'world'}, 200

api.add_resource(Homepage, '/')

class ActualsData(Resource):
    """
    API endpoint for "actuals" data.
    """
    def get(self):
        """
        GET method.
        Returns "actual" data in json format, if requested data is valid. 
        Returns status code, 400, otherwise.
        """
        if not actuals_data:
            abort(400, message="Invalid request")
        else:
            return actuals_data, 200

api.add_resource(ActualsData, '/get_actuals_data/')

if __name__ == '__main__':
    app.run(debug=True)

# Environment variable (Done)
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

    # 2 Drop down list, Actuals (Jeff) (Done)
        # State
            # Actuals
                # Make HospitalBeds and icuBeds be list

# API End point Flask restful api

    # State selection   (Greg)

    # General profile   (Greg)

    # Actuals selection (Jeff) (Done)

# Deploy
    # Heroku