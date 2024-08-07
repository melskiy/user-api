from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    async def create_item(self, item):
        pass

    @abstractmethod
    async def read_item(self, item_id):
        pass

    @abstractmethod
    async def update_item(self, item):
        pass

    @abstractmethod
    async def delete_item(self, item_id):
        pass
