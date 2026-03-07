import json
import os
from jsonschema import validate
def validate_schema(data, schema_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, schema_path)
    with open(full_path) as file:
        schema = json.load(file)
    validate(instance=data, schema=schema)