from dataclasses import dataclass
from typing import Dict
import mysql.connector  # type: ignore

from app.utils.config import get_yaml_config
from app.exceptions import DatabaseConnectionError


@dataclass
class Database:
    def __init__(self) -> None:
        db_config: Dict = get_yaml_config("app/credentials.yaml")["database"]
        try:
            self.database = mysql.connector.connect(host=db_config["host"], database=db_config["database"],
                                                    user=db_config["user"], password=db_config["password"])
        except Exception as error:
            raise DatabaseConnectionError(error)
        self.cursor = self.database.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.database.close()

    def commit(self) -> None:
        self.database.commit()
