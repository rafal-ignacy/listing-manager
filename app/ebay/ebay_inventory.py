from dataclasses import dataclass
from typing import List

from app.web_requests.web_requests import WebRequests
from app.ebay.ebay_auth import EbayAuth


@dataclass
class EbayInventory:
    def __init__(self) -> None:
        self.web_requests: WebRequests = WebRequests()
        self.ebay_auth: EbayAuth = EbayAuth()

    def create_inventory_item(self, platform_id: str, inventory_id: int, type: str, picture_urls: List):
        access_token: str = self.ebay_auth.get_access_token()
        self.web_requests.ebay_create_inventory_item(access_token, platform_id, inventory_id, type, picture_urls)
