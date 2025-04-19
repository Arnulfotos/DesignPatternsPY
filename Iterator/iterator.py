from abc import ABC,abstractmethod
from typing import Any, List

class Iterator(ABC):
    @abstractmethod
    def next(self) -> any:
        pass
    @abstractmethod
    def has_next(self) -> bool:
        pass

class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


class ConcreteCollection(IterableCollection):
    def __init__(self, items: List[Any]):
        self._items = items

    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self)

    def get_items(self)-> List[Any]:
        return self._items


class ConcreteIterator(Iterator):
    def __init__(self, collection: ConcreteCollection):
        self._collection = collection
        self._index = 0

    def next(self) -> Any:
        if self.has_next():
            items = self._collection.get_items()[self._index]
            self._index += 1
            return items

    def has_next(self) -> bool:
        return self._index < len(self._collection.get_items())


collection = ConcreteCollection(["juan","pedro", "ana"])
iterator = collection.create_iterator()

while iterator.has_next():
    print(iterator.next())
