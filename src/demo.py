from dewco import domain
import json

values = []
values.append(domain.Value("temp", 22))

systems = []
systems.append(domain.System.fromSuccess("PI", values))
systems.append(domain.System.fromError("Hat", "Power failure"))

r = domain.Result.fromSuccess(systems)

js = json.dumps(r, default=lambda x: x.__dict__, indent=4)

print(js)