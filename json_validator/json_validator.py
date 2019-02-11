import jsonschema
from jsonschema import validate
import json

with open("j_schema.json") as fd:
    schema = json.load(fd)

with open("example.json") as fd:
    eg = json.load(fd)

print(schema)

try:
    validate(eg, schema)
except Exception as e:
    print(e)
