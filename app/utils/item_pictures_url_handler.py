from dataclasses import dataclass
from string import Template
from typing import List
import requests

from app.utils.config import get_yaml_config
from app.exceptions import NoPicturesOnHosting, HostingCommunicationError


@dataclass
class ItemPicturesUrlHandler:
    def __init__(self, inventory_id: int, type: str) -> None:
        self.inventory_id: int = inventory_id
        self.type: str = type
        self.url_template: Template = Template(get_yaml_config("app/config.yaml")["item_pictures_url_handler"]["url_template"])

    def get_urls(self) -> str:
        picture_index: int = 1
        picture_id_prefix: str = str(self.inventory_id) + self.type + "-"
        pictures_urls_list: List = []
        while True:
            picture_id: str = picture_id_prefix + str(picture_index)
            url: str = self.url_template.substitute(picture_id=picture_id)
            try:
                request: requests.Response = requests.get(url)
            except Exception as error:
                raise HostingCommunicationError(error)
            if request.status_code != 200:
                break
            pictures_urls_list.append(url)
            picture_index += 1
        if len(pictures_urls_list) == 0:
            raise NoPicturesOnHosting
        pictures_urls_str: str = ";".join(pictures_urls_list)
        return pictures_urls_str
