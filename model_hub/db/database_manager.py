from abc import abstractmethod
from typing import List

from model_hub.db.models import Model


class DatabaseManager:
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(self, path: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass

    @abstractmethod
    async def get_models(self) -> List[Model]:
        pass

    @abstractmethod
    async def get_model(self, model_url: str) -> Model:
        pass

    @abstractmethod
    async def add_model(self, model: Model):
        pass

    @abstractmethod
    async def update_model(self, model_url: str, model: Model):
        pass

    @abstractmethod
    async def delete_model(self, model_url: str):
        pass
