from .systemcontroller import SystemController

from typing import List

class SystemsService:
    def __init__(self, controllers: List[SystemController]):
        self.controllers = []
        if controllers != None:
            self.controllers = controllers.copy()
