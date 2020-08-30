#apidata.py>
import requests

#functions
def get_api_status(inputarg):
    r = requests.get("https://api.covidtracking.com/v1/status.json")
    print(r)
    return None
