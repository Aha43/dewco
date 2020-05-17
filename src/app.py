#!/usr/bin/python3

import json
import sys
from typing import List

import flask

from dewco import domain
from dewco.rest_util import Result
from dewco.systems.handlers import SystemHandlers, add_common_system_handlers
from dewco.systems.sensehat.sense_hat_handlers import add_sense_hat_handlers

def get_systems_from_query() -> List[str]: 
    systemsQuery = flask.request.args.get("systems")
    if systemsQuery == None:
        return []
    return systemsQuery.split(',')

def get_result_json(result: object) -> str:
    if result == None:
        raise TypeError("result is None")
    retVal = json.dumps(result, default=lambda x: x.__dict__, indent=4)
    return retVal

def respond(result: Result) -> str:
    json = get_result_json(result)
    response = app.response_class(json, status = 200, mimetype = 'application/json')
    return response

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
        result = Result.from_error(message)
    return respond(result)

@app.route('/state', methods=['GET'])
def getState():
    system = get_systems_from_query()
    result = None
    try:
        states = []
        for s in system:
            if s in systemHandlers:
                states.append(systemHandlers[s].state())
        result = Result.from_success(states)
    except:
        message = sys.exc_info()[0]
        result = Result.from_error(message)
    return respond(result)

@app.route('/state', methods=['POST'])
def postState():
    result = Result.from_success()
    try:
        req = flask.request.get_json()
        for dict in req:       
            system = domain.System.from_dict(dict)
            if system.name in systemHandlers:
                message = systemHandlers[system.name].action(system)
                if message and len(message) > 0: 
                    result = Result.from_error(message)
                    break
    except:
        message = sys.exc_info()[0]
        result = Result.from_error(message)
    return respond(result)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
