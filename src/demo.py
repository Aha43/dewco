from dewco import domain
import json

values = []
values.append(domain.Value("temp", 22))
#r = domain.Result(True, "All cool", domain.System.fromSuccess("PI", values), domain.System.fromError("Hat", "Power failure"))

systems = []
systems.append(domain.System.fromSuccess("PI", values))
systems.append(domain.System.fromError("Hat", "Power failure"))

r = domain.Result.fromSuccess(systems)

js = json.dumps(r, default=lambda x: x.__dict__, indent=4)

print(js)