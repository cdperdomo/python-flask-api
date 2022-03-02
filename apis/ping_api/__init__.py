from flask import Blueprint

ping_api_blueprint = Blueprint('ping_api', __name__)

from . import ping_api