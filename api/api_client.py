import requests
from utils.config_reader import get_config

config = get_config()

class APIClient:

    def __init__(self):
        self.base_url = config["base_url"]
        self.headers = {
            "User-Agent": "pytest-api-framework",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = self.base_url + endpoint
        print("Request URL:", url)
        return requests.get(url, headers=self.headers)

    def post(self, endpoint, payload=None):
        return requests.post(self.base_url + endpoint, json=payload, headers=self.headers)



