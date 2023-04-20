from dataclasses import dataclass
import time
from singleton_decorator import singleton  # type: ignore

from app.web_requests.web_requests import WebRequests
from app.exceptions import CannotGetEbayAccessToken


@singleton
@dataclass
class EbayAuth:
    def __init__(self) -> None:
        self.web_requests = WebRequests()
        self.access_token_request_time: float = 0
        self.access_token_validity_time: int = 7200

    def get_access_token(self) -> str:
        now: float = time.time()
        if now - self.access_token_request_time > self.access_token_validity_time - 10:
            try:
                self.access_token = self.web_requests.ebay_get_access_token()
            except Exception as error:
                raise CannotGetEbayAccessToken(error)
            self.access_token_request_time = time.time()
            return self.access_token
        else:
            return self.access_token
