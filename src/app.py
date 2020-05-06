import flask
import sys
from dewco import services, domain, controllers, sense_hat_controller
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

platformController = controllers.PlatformSystemController()
senseHatController = sense_hat_controller.SenseHatSystemController()
controllers = [platformController, senseHatController]
service = services.SystemsService(controllers)

@app.route('/', methods=['GET'])
def get():
    result = None
    try:
        status = service.status()
        result = domain.Result.fromSuccess(status)
    except:
        message = sys.exc_info()[0]
        result = domain.Result.fromError(message)

    response = app.response_class(
        response = json.dumps(result, default=lambda x: x.__dict__, indent=4),
        status = 200,
        mimetype='application/json'
    )

    return response

app.run(host = '0.0.0.0', port = 8090)
