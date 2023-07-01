from dataclasses import dataclass
from typing import Dict


@dataclass
class ResponseHandler:
    def ebay_get_access_token(self, response: Dict) -> str:
        return response["access_token"]

    def exchange_currency(self, response: Dict, currency: str) -> float:
        return response["rates"][currency]
