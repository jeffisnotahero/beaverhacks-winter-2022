from dotenv import dotenv_values
import requests

# Enviroment variable
config = dotenv_values(".env")
api_key = config["API_KEY"]

def request_api_data():
    """
    Requests external API and return data in dict format.
    Returns None if request is not valid.
    https://covidactnow.org/data-api
    """
    try:
        data = requests.get(f"https://api.covidactnow.org/v2/states.json?apiKey={api_key}")
        json = data.json()
        return json
    except requests.exceptions.RequestException as error:
        print(error.response.text)
        return None

def filter_actuals_data(json):
    """
    Filter "actuals" data from input, taken as parameter, and return it in dict format.
    Return None if input is not valid.
    """
    if not json:
        return None
    
    actuals_data = {}
    for entry in json:
            actuals_data[entry["state"]] = {"actuals": 
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
                }}
                
    return actuals_data