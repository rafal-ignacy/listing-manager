from dataclasses import dataclass
import math

from app.web_requests.web_requests import WebRequests


@dataclass
class PriceExchangeHandler:
    def get_price(self, price_eur: float, platform_id: str) -> float:
        web_requests = WebRequests()
        match platform_id:
            case "EBAY_US":
                currency: str = "USD"
                currency_value: float = web_requests.exchange_currency(currency)
            case "EBAY_GB":
                currency: str = "GBP"                                             # type: ignore
                currency_value: float = web_requests.exchange_currency(currency)  # type: ignore
            case "EBAY_DE" | "ETSY":
                return price_eur
        final_price: float = price_eur * currency_value
        return math.ceil(final_price)
