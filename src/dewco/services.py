from .domain import System
from .controllers import SystemController

from typing import List

class SystemsService:
    def __init__(self, controllers: List[SystemController]):
        self.controllers = dict()
        if controllers != None:
            for c in controllers:
                self.controllers[c.name] = c

    def status(self, systemNames: List[str] = None) -> List[System]:
        retVal = []
        if systemNames == None :
            systemNames = self.controllers.keys()
        for name in systemNames:
            if name in self.controllers:
                c = self.controllers[name]
                if c != None:
                    statuses = c.status()
                    for s in statuses:
                        retVal.append(s)
        return retVal  
