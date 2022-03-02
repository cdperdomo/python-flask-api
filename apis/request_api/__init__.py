from flask import Blueprint

request_api_blueprint = Blueprint('request_api', __name__)

from . import request_api

