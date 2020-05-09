#!/usr/bin/env python

import importlib
from .util import get_env_var

senseHatModule = get_env_var("__sense_hat_module__", "sense_hat")
sense_module = importlib.import_module(senseHatModule)
#sense_module = importlib.import_module("dewco.sense_dummy")

from .controllers import SystemController
from typing import List
from .domain import System, Value

class SenseHatSystemController(SystemController):
	def __init__(self):
		super().__init__("SenseHat")

	def status(self) -> List[System]:

		retVal = []
		state = []
		sense = self.__get_sense_system()
		state.append(Value.readOnly("system-name", "SenseHat"))
		available = sense != None
		state.append(Value.readOnly("available", available))
		if available:
			state.append(Value.readOnly("humidity", sense.get_humidity()))
		retVal.append(System.fromSuccess(self.name, state))
		return retVal

	def __get_sense_system(self):
		try:
			return sense_module.SenseHat()
		except:
			return None
