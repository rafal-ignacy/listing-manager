from dataclasses import dataclass
from typing import Dict, Optional
import requests

from app.exceptions import RequestError, RequestNotCorrectError


@dataclass
class WebRequest:
    url: str
    headers: Optional[Dict] = None
    payload: Optional[Dict] = None

    def execute(self, method_type: str) -> Dict | bytes | None:
        try:
            match method_type:
                case "POST":
                    request = requests.post(self.url, headers=self.headers, data=self.payload, timeout=10)
                case "PUT":
                    request = requests.put(self.url, headers=self.headers, json=self.payload, timeout=10)
                case "GET":
                    request = requests.get(self.url, headers=self.headers, data=self.payload, timeout=10)
                case "DELETE":
                    request = requests.delete(self.url, headers=self.headers, data=self.payload, timeout=10)
        except Exception as error:
            raise RequestError(method_type + " " + str(error))

        if request.ok:
            if request.headers.get("Content-Type") == "application/json" or request.headers.get("Content-Type") == "application/json; charset=utf-8":
                try:
                    return request.json()
                except Exception:
                    return None
            else:
                return request.content
        else:
            raise RequestNotCorrectError(str(request.status_code) + " " + request.text)
