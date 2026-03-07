import os
import yaml

def get_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path) as file:
        return yaml.safe_load(file)