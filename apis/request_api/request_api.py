import logging
import os

from flask import request
from flask import jsonify
from . import request_api_blueprint


@request_api_blueprint.route('/request', methods=['GET'])
def hello_world():  # put application's code here
    var = {}
    for k, v in request.headers:
        var[k] = v
    print('Http Headers: ', var)
    print('ENV: USER=', os.getenv('JAVA_HOME', 'DEFAULT'))
    logging.info('ENV: USER=', os.getenv('JAVA_HOME', 'DEFAULT'))

    return jsonify(
                headers=var,
                method=request.method
            )
