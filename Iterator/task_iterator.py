from abc import ABC,abstractmethod
from typing import Any, List
import time

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


class TaskList(IterableCollection):
    def __init__(self, tasks: List[Any]):
        self.__tasks = tasks

    def create_iterator(self) -> Iterator:
        return TaskIterator(self)

    def get_task(self) -> List[Any]:
        return self.__tasks

class TaskIterator(Iterator):
    def __init__(self,task_list: TaskList):
        self.task_list = task_list
        self.index = 0

    def next(self) -> Any:
        if self.has_next():
            items = self.task_list.get_task()[self.index]
            self.index += 1
            return items()

    def has_next(self) -> bool:
        return self.index < len(self.task_list.get_task())


def task1():
    return "Tarea 1 se ejecuta"

def task2():
    return "Tarea 2 se ejecuta"

def task3():
    return "Tarea 3 se ejecuta"

task = [task1,task2, task3]

task_list = TaskList(task)

task_itr = task_list.create_iterator()

while task_itr.has_next():
    print(task_itr.next())
    time.sleep(3)
