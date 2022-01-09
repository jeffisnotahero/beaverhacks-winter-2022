from os import stat_result
from dotenv.main import dotenv_values
from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api, abort

from helper import request_api_data, filter_actuals_data, filter_state_entry, filter_actuals_entry

app = Flask(__name__)
api = Api(app)

json = request_api_data()

actuals_data = filter_actuals_data(json)

actuals_entry = filter_actuals_entry(actuals_data)
state_entry = filter_state_entry(actuals_data)

@app.route("/")
def index():
    return render_template("index.html")

class Homepage(Resource):
    """
    API endpoint for homepage.
    """
    def get(self):
        """
        GET method.
        """
        return {'hello': 'world'}, 200

api.add_resource(Homepage, '/hello')

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

class StateEntry(Resource):
    """
    API endpoint for "state" data.
    """
    def get(self):
        """
        GET method.
        Returns "state" data in json format, if requested data is valid. 
        Returns status code, 400, otherwise.
        """
        if not state_entry:
            abort(400, message="Invalid request")
        else:
            return state_entry, 200

api.add_resource(StateEntry, '/get_state_entry/')

class ActualsEntry(Resource):
    """
    API endpoint for "actuals" entry.
    """
    def get(self):
        """
        GET method.
        Returns "actuals" entry in json format, if requested data is valid. 
        Returns status code, 400, otherwise.
        """
        if not actuals_entry:
            abort(400, message="Invalid request")
        else:
            return actuals_entry, 200

api.add_resource(ActualsEntry, '/get_actuals_entry/')

class ActualsEntryData(Resource):

    def get(self, state, data):
        if not data and not state:
            abort(400, message="Invalid request")
        
        if state not in actuals_data and data not in actuals_data[state]["actuals"]:
            abort(400, message="No such data")

        value = actuals_data[state]["actuals"][data]
        response = {"data": [value]}
        return response, 200

api.add_resource(ActualsEntryData, "/get_actuals_entry_data/<string:state>/actuals/<string:data>")

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