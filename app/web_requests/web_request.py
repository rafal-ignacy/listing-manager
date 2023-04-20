from dataclasses import dataclass
from typing import Dict, Optional
import requests

from app.exceptions import RequestError, RequestNotCorrectError


@dataclass
class WebRequest:
    url: str
    headers: Optional[Dict] = None
    payload: Optional[Dict] = None

    def response(self):
        try:
            if self.payload is not None:
                request = requests.post(self.url, headers=self.headers, data=self.payload, timeout=10)
            else:
                request = requests.get(self.url, headers=self.headers, timeout=10)
        except Exception as error:
            raise RequestError(error)

        if request.ok:
            if request.headers.get("Content-Type") == "application/json" or request.headers.get("Content-Type") == "application/json; charset=utf-8":
                return request.json()
            else:
                return request.content
        else:
            raise RequestNotCorrectError(request.status_code + " " + request.text)
