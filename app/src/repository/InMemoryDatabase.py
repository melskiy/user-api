from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.models.user import User

class InMemoryDatabase(RepositoryInterface):
    def __init__(self):
        self.items = []

    async def create_item(self, user: User):
        self.items.append(user)
        print(self.items)

    async def read_item(self, item_id: int):
        for item in self.items:
            if item.user_id == item_id:
                return item
        return None

    async def update_item(self, item_id: int, user: User):
        for item in self.items:
            if item.user_id == item_id:
                self.items[self.items.index(item)] = user
                return item
        return None

    async def delete_item(self, item_id: int) -> bool:
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                break
        return None
