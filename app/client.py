# client.py>
import requests

class CovidTrackingClient:
    url = ''

    def __init__(self, url):
        self.url = url

    # functions
    def get_api_status(self):
        r = requests.get(self.url + '/v1/status.json')
        return r.json()

    def get_data(self):
        return None

    def get_historic_data_by_date(self, date_request):
        r = requests.get(self.url + '/v1/us/' + date_request.date + '.json')
        return r.json()