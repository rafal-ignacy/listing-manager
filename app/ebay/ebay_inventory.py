from dataclasses import dataclass
from typing import List

from app.web_requests.web_requests import WebRequests
from app.ebay.ebay_auth import EbayAuth
from app.utils.listing_description_handler import ListingDescriptionHandler
from app.utils.price_exchange_handler import PriceExchangeHandler


@dataclass
class EbayInventory:
    def __init__(self) -> None:
        self.web_requests: WebRequests = WebRequests()
        self.ebay_auth: EbayAuth = EbayAuth()

    def create_inventory_item(self, platform_id: str, inventory_id: int, type: str, picture_urls: List):
        access_token: str = self.ebay_auth.get_access_token()
        self.web_requests.ebay_create_inventory_item(access_token, platform_id, inventory_id, type, picture_urls)

    def create_offer(self, platform_id: str, inventory_id: int, type: str, price: float, dimensions: str):
        access_token: str = self.ebay_auth.get_access_token()
        listing_description_handler: ListingDescriptionHandler = ListingDescriptionHandler()
        listing_description: str = listing_description_handler.create_description(platform_id, type, dimensions)
        price_exchange_handler: PriceExchangeHandler = PriceExchangeHandler()
        price = price_exchange_handler.get_price(price, platform_id)
        offer_id: str = self.web_requests.ebay_create_offer(access_token, platform_id, inventory_id, type, listing_description, price)
        return offer_id

    def publish_offer(self, offer_id: str):
        access_token: str = self.ebay_auth.get_access_token()
        listing_id: str = self.web_requests.ebay_publish_offer(access_token, offer_id)
        return listing_id
