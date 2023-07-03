from dataclasses import dataclass

from app.data.db import Database
from app.data_models.item import Item
from app.utils.config import get_yaml_config
from app.exceptions import DatabaseAddItemError, DatabaseGetItemsError


@dataclass
class DataRepository:
    def add_item(self, item: Item) -> None:
        db_query: str = get_yaml_config("app/data/db_queries.yaml")["add_item"]
        with Database() as database:
            try:
                database.cursor.execute(db_query, item.__dir__())
                database.commit()
            except Exception as error:
                raise DatabaseAddItemError(error)

    def get_items(self):
        db_query: str = get_yaml_config("app/data/db_queries.yaml")["get_items"]
        with Database() as database:
            try:
                database.cursor.execute(db_query)
                rows = database.cursor.fetchall()
            except Exception as error:
                raise DatabaseGetItemsError(error)
        return rows
