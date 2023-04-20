from dataclasses import dataclass

from app.web_requests.urls import Urls
from app.web_requests.headers import Headers
from app.web_requests.payloads import Payloads
from app.web_requests.web_request import WebRequest
from app.web_requests.response_handler import ResponseHandler


@dataclass
class WebRequests:
    def __init__(self):
        self.urls = Urls("app/web_requests/config/urls.yaml")
        self.headers = Headers("app/web_requests/config/headers.json", "app/credentials.yaml")
        self.payloads = Payloads("app/web_requests/config/payloads.json", "app/credentials.yaml")
        self.response_handler = ResponseHandler()

    def ebay_get_access_token(self) -> str:
        url = self.urls.ebay_get_access_token()
        headers = self.headers.ebay_get_access_token()
        payload = self.payloads.ebay_get_access_token()

        web_request = WebRequest(url, headers, payload)
        response_content = web_request.response()
        return self.response_handler.ebay_get_access_token(response_content)
