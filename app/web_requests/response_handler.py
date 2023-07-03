from dataclasses import dataclass
from typing import Dict


@dataclass
class ResponseHandler:
    def ebay_get_access_token(self, response: Dict) -> str:
        return response["access_token"]

    def ebay_create_offer(self, response: Dict) -> str:
        return response["offerId"]

    def ebay_publish_offer(self, response: Dict) -> str:
        return response["listingId"]

    def exchange_currency(self, response: Dict, currency: str) -> float:
        return response["rates"][currency]
