from dataclasses import dataclass
from typing import Dict, List

from app.utils.config import get_yaml_config, get_json_config
from app.utils.json_template import JsonTemplate


@dataclass
class Payloads:
    def __init__(self, payloads_file_path, credentials_file_path) -> None:
        self.__payloads = get_json_config(payloads_file_path)
        self.__credentials = get_yaml_config(credentials_file_path)

    def ebay_get_access_token(self) -> Dict:
        json_template: JsonTemplate = JsonTemplate(self.__payloads["ebay_get_access_token"])
        payload: Dict = json_template.generate({"refresh_token": self.__credentials["ebay_refresh_token"]})
        return payload

    def ebay_create_inventory_item(self, platform_id: str, inventory_id: int, type: str, picture_urls: List) -> Dict:
        json_template: JsonTemplate = JsonTemplate(self.__payloads["ebay_create_inventory_item"][platform_id][type])
        payload: Dict = json_template.generate({"inventory_id": inventory_id, "pictures_urls": picture_urls})
        return payload

    def ebay_create_offer(self, platform_id: str, inventory_id: int, type: str, listing_description: str, price: float) -> Dict:
        json_template: JsonTemplate = JsonTemplate(self.__payloads["ebay_create_offer"][platform_id][type])
        payload: Dict = json_template.generate({"sku": str(inventory_id) + type, "listing_description": listing_description, "price": str(price)})
        return payload
