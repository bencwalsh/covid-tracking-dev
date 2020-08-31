from flask import Flask
from .client import CovidTrackingClient
from .model import DateRequest

BASE_URL = 'https://api.covidtracking.com'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    client = CovidTrackingClient(BASE_URL)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route('/')
    def hello():
        return client.get_api_status()

    @app.route('/date')
    def date():
        r = DateRequest('20200601')
        return client.get_historic_data_by_date(r)

    return app
