from abc import abstractmethod
from services.database.SQLService import SQLService


class Service:
    sql = None

    def __init__(self) -> None:
        if self.sql is None:
            self.sql = SQLService()
        super().__init__()

    @abstractmethod
    def findAll(self):
        return
