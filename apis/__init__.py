from flask import Flask
from . import request_api
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .request_api import request_api_blueprint
        from .ping_api import ping_api_blueprint

        # add
        app.register_blueprint(request_api_blueprint)
        app.register_blueprint(ping_api_blueprint)

        return app
