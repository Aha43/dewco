from dewco import domain, systemcontroller
import json

values = []
values.append(domain.Value("temp", 22))

platformController = systemcontroller.PlatformSystemController()

systems = []
for s in platformController.status():
    systems.append(s)
systems.append(domain.System.fromError("Hat", "Power failure"))

r = domain.Result.fromSuccess(systems)

js = json.dumps(r, default=lambda x: x.__dict__, indent=4)

print(js)