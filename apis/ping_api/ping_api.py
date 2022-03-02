from . import ping_api_blueprint


@ping_api_blueprint.route('/ping', methods=['GET'])
def ping():  # put application's code here
    return "ok"
