from dataclasses import dataclass
from typing import List, Dict

from app.web_requests.urls import Urls
from app.web_requests.headers import Headers
from app.web_requests.payloads import Payloads
from app.web_requests.web_request import WebRequest
from app.web_requests.response_handler import ResponseHandler
from app.exceptions import CannotGetEbayAccessToken, CannotCreateEbayInventoryItem, CannotCreateEbayOffer, CannotExchangeCurrency, CannotPublishEbayOffer


@dataclass
class WebRequests:
    def __init__(self):
        self.urls: Urls = Urls("app/web_requests/config/urls.yaml")
        self.headers: Headers = Headers("app/web_requests/config/headers.json", "app/credentials.yaml")
        self.payloads: Payloads = Payloads("app/web_requests/config/payloads.json", "app/credentials.yaml")
        self.response_handler: ResponseHandler = ResponseHandler()

    def ebay_get_access_token(self) -> str:
        url: str = self.urls.ebay_get_access_token()
        headers: Dict = self.headers.ebay_get_access_token()
        payload: Dict = self.payloads.ebay_get_access_token()
        web_request: WebRequest = WebRequest(url, headers, payload)
        try:
            response_content = web_request.execute("POST")
        except Exception as error:
            raise CannotGetEbayAccessToken(error)
        return self.response_handler.ebay_get_access_token(response_content)  # type: ignore

    def ebay_create_inventory_item(self, access_token: str, platform_id: str, inventory_id: int, type: str, picture_urls: List) -> None:
        url: str = self.urls.ebay_create_inventory_item(inventory_id, type)
        headers: Dict = self.headers.ebay_create_inventory_item(access_token, platform_id)
        payload: Dict = self.payloads.ebay_create_inventory_item(platform_id, inventory_id, type, picture_urls)
        web_request: WebRequest = WebRequest(url, headers, payload)
        try:
            web_request.execute("PUT")
        except Exception as error:
            raise CannotCreateEbayInventoryItem(error)

    def ebay_create_offer(self, access_token: str, platform_id: str, inventory_id: int, type: str, listing_description: str, price: float) -> str:
        url: str = self.urls.ebay_create_offer()
        headers: Dict = self.headers.ebay_create_offer(access_token, platform_id)
        payload: str = self.payloads.ebay_create_offer(platform_id, inventory_id, type, listing_description, price)
        web_request: WebRequest = WebRequest(url, headers, payload)
        try:
            response_content = web_request.execute("POST")
        except Exception as error:
            raise CannotCreateEbayOffer(error)
        offer_id: str = self.response_handler.ebay_create_offer(response_content)  # type: ignore
        return offer_id

    def ebay_publish_offer(self, access_token: str, offer_id: str) -> str:
        url: str = self.urls.ebay_publish_offer(offer_id)
        headers: Dict = self.headers.ebay_publish_offer(access_token)
        web_request: WebRequest = WebRequest(url, headers)
        try:
            response_content = web_request.execute("POST")
        except Exception as error:
            raise CannotPublishEbayOffer(error)
        listing_id: str = self.response_handler.ebay_publish_offer(response_content)  # type: ignore
        return listing_id

    def exchange_currency(self, currency: str) -> float:
        url: str = self.urls.exchange_currency()
        web_request: WebRequest = WebRequest(url)
        try:
            response_content = web_request.execute("GET")
        except Exception as error:
            raise CannotExchangeCurrency(error)
        return self.response_handler.exchange_currency(response_content, currency)  # type: ignore
