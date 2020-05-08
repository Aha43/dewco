try:
	from sense_hat import SenseHat
	print(">>>>Imported real sense hat")
except:
	try:
		from sense_emu import SenseHat
		print(">>>>Imported emulator sense hat")
	except ImportError:
		from .sense_dummy import SenseHat
		print(">>>>Import dummy sense hat")

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
			return SenseHat()
		except:
			return None
