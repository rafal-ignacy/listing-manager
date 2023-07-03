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

    def ebay_publish_offer(self, offer_id: str) -> str:
        url: str = self.__urls["ebay_publish_offer"].replace("{offer_id}", offer_id)
        return url

    def exchange_currency(self) -> str:
        url: str = self.__urls["exchange_currency"]
        return url
