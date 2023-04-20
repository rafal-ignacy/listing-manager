from dataclasses import dataclass
from typing import Dict
import json
from json_templates import JsonTemplates  # type: ignore
from enum import IntEnum

from app.utils.config import get_yaml_config, get_json_config


class Json(IntEnum):
    Output = 1


@dataclass
class Headers:
    def __init__(self, headers_file_path: str, credentials_file_path: str) -> None:
        self.__headers: Dict = get_json_config(headers_file_path)
        self.__credentials: Dict = get_yaml_config(credentials_file_path)

    def ebay_get_access_token(self) -> Dict:
        json_template: JsonTemplates = JsonTemplates()
        json_template.loads(json.dumps(self.__headers["get_ebay_access_token"]))
        headers: Dict = json_template.generate({"base64_encoded_credentials": self.__credentials["ebay_base64_encoded_credentials"]})[Json.Output]
        return headers
