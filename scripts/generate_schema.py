import requests
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.schema_generator import generate_schema



response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()

# generate schema from first user
generate_schema(data[0], "schemas/user_schema.json")