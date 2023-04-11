from dataclasses import dataclass
from typing import Tuple


@dataclass
class Item:
    inventory_id: int
    type: str
    price: float
    dimensions: str
    picture_urls: str

    def __dir__(self) -> Tuple:
        return (self.inventory_id, self.type, self.price, self.dimensions, self.picture_urls)
