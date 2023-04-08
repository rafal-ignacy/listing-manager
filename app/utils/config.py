import yaml
from typing import Dict

from app.settings import ROOT_DIR


def get_config(path) -> Dict:
    with open(ROOT_DIR + path, "r") as config_file:
        return yaml.safe_load(config_file)
