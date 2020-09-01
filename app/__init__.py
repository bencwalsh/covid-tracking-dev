from flask import Flask
from flask_assets import Environment

from .blueprints import index
from .util import bundles


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    _load_config(app, test_config)
    _load_blueprints(app)
    _load_assets(app)

    return app


def _load_config(app, test_config):
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


def _load_blueprints(app):
    app.register_blueprint(index)


def _load_assets(app):
    assets = Environment(app)
    assets.register(bundles)
