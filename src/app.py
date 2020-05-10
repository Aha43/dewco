#!/usr/bin/python3

import json
import sys
import flask
from typing import List

from dewco import domain
from dewco.systems.handlers import SystemHandlers, add_common_system_handlers
from dewco.systems.sense_hat import add_sense_hat_handlers

app = flask.Flask(__name__)
app.config["DEBUG"] = True

systemHandlers = dict()
add_common_system_handlers(systemHandlers)
add_sense_hat_handlers(systemHandlers)

@app.route('/system', methods=['GET'])
def getSystem():
    result = None
    try:
        systems = []
        for h in systemHandlers.values():
            name = h.name
            systems.append(name)
        result = domain.Result.from_success(systems)
    except:
        message = sys.exc_info()[0]
        result = domain.Result.from_error(message)

    json = getResultJSON(result)
    response = app.response_class(json, status = 200, mimetype='application/json')

    return response

def get_systems_from_query() -> List[str]: 
    systemsQuery = flask.request.args.get("systems")
    if systemsQuery == None:
        return []
    return systemsQuery.split(',')

@app.route('/state', methods=['GET'])
def getState():
    system = get_systems_from_query()
    print(system)
    result = None
    try:
        states = []
        for s in system:
            if s in systemHandlers:
                states.append(systemHandlers[s].state())
        result = domain.Result.from_success(states)
    except:
        message = sys.exc_info()[0]
        result = domain.Result.from_error(message)

    json = getResultJSON(result)
    response = app.response_class(json, status = 200, mimetype='application/json')

    return response

def getResultJSON(result: object) -> str:
    if result == None:
        raise TypeError("result is None")
    retVal = json.dumps(result, default=lambda x: x.__dict__, indent=4)
    return retVal

app.run(host = '0.0.0.0', port = 8090)
