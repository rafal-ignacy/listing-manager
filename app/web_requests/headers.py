from dataclasses import dataclass
from typing import Dict

from app.utils.config import get_yaml_config, get_json_config
from app.utils.json_template import JsonTemplate


@dataclass
class Headers:
    def __init__(self, headers_file_path: str, credentials_file_path: str) -> None:
        self.__headers: Dict = get_json_config(headers_file_path)
        self.__credentials: Dict = get_yaml_config(credentials_file_path)

    def ebay_get_access_token(self) -> Dict:
        json_template: JsonTemplate = JsonTemplate(self.__headers["ebay_get_access_token"])
        headers: dict = json_template.generate({"base64_encoded_credentials": self.__credentials["ebay_base64_encoded_credentials"]})
        return headers

    def ebay_create_inventory_item(self, access_token: str, platform_id: str) -> Dict:
        json_template: JsonTemplate = JsonTemplate(self.__headers["ebay_create_inventory_item"][platform_id])
        headers: Dict = json_template.generate({"access_token": access_token})
        return headers

    def ebay_create_offer(self, access_token: str, platform_id: str) -> Dict:
        json_template: JsonTemplate = JsonTemplate(self.__headers["ebay_create_offer"][platform_id])
        headers: Dict = json_template.generate({"access_token": access_token})
        return headers