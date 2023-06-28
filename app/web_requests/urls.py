from dataclasses import dataclass
from typing import Dict

from app.utils.config import get_yaml_config


@dataclass
class Urls:
    def __init__(self, urls_file_path: str) -> None:
        self.__urls: Dict = get_yaml_config(urls_file_path)

    def ebay_get_access_token(self) -> str:
        url: str = self.__urls["ebay_get_access_token"]
        return url

    def ebay_create_inventory_item(self, inventory_id: int, type: str):
        url: str = self.__urls["ebay_create_inventory_item"].replace("{sku}", str(inventory_id) + type)
        return url

    def ebay_create_offer(self) -> str:
        url: str = self.__urls["ebay_create_offer"]
        return url