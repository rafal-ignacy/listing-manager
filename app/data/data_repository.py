from dataclasses import dataclass

from app.data.db import Database
from app.data_models.item import Item
from app.utils.config import get_config
from app.exceptions import DatabaseAddItemError


@dataclass
class DataRepository:
    def add_item(self, item: Item) -> None:
        db_query: str = get_config("app/data/db_queries.yaml")["add_item"]
        with Database() as database:
            try:
                database.cursor.execute(db_query, item.__dir__())
                database.commit()
            except Exception as error:
                raise DatabaseAddItemError(error)


data = DataRepository()
data.add_item(Item(1, "K", 50, "50;50;50", "http://test.com"))