import os
from flask import Flask

from .api.routes import api
from .site.routes import site

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_PATH, 'resources/templates/')
STATIC_PATH = os.path.join(BASE_PATH, 'static/')

def create_app():
    app = Flask(__name__, static_folder = STATIC_PATH, template_folder = TEMPLATE_PATH)

    app.register_blueprint(api)
    app.register_blueprint(site)

    return app
