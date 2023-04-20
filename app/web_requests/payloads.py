from dataclasses import dataclass
from typing import Dict
import json
from json_templates import JsonTemplates  # type: ignore
from enum import IntEnum

from app.utils.config import get_yaml_config, get_json_config


class Json(IntEnum):
    Output = 1


@dataclass
class Payloads:
    def __init__(self, payloads_file_path, credentials_file_path) -> None:
        self.__payloads = get_json_config(payloads_file_path)
        self.__credentials = get_yaml_config(credentials_file_path)

    def ebay_get_access_token(self) -> Dict:
        json_template: JsonTemplates = JsonTemplates()
        json_template.loads(json.dumps(self.__payloads["get_ebay_access_token"]))
        payload: Dict = json_template.generate({"refresh_token": self.__credentials["ebay_refresh_token"]})[Json.Output]
        return payload
