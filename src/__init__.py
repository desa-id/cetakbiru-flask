import os
from flask import Flask

from .api.routes import api
from .site.routes import site

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(site)

    return app
