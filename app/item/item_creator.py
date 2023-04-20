from dataclasses import dataclass

from app.data_models.item import Item
from app.utils.item_pictures_url_handler import ItemPicturesUrlHandler
from app.exceptions import ItemObjectNotCreated


@dataclass
class ItemCreator:
    def create_item(self, inventory_id: int, type: str, price: float, dimensions: str) -> Item:
        item_pictures_url_handler: ItemPicturesUrlHandler = ItemPicturesUrlHandler(inventory_id, type)
        try:
            pictures_url: str = item_pictures_url_handler.get_urls()
        except Exception as error:
            raise ItemObjectNotCreated(error)
        return Item(inventory_id, type, price, dimensions, pictures_url)
