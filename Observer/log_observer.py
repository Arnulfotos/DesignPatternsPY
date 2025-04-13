from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def refresh(self, subject):
        pass



class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            print("El observador no existe")

    def notify(self):
        for observer in self._observers:
            observer.refresh(self)


class System(Subject):
   def __init__(self):
       super().__init__()
       self._state = None

   @property
   def state(self):
        return self._state

   @state.setter
   def state(self,value):
       self._state = value
       self.notify()


class FileObserver(Observer):
    def __init__(self, file_path):
        self.file_path = file_path

    def refresh(self, subject):
        with open(self.file_path, "a") as file:
            file.write(f"Estado del sistema {subject.state}\n")

class ConsoleObserver(Observer):
    def refresh(self, subject):
            print(f"Estado del sistema {subject.state}\n")



file_obs = FileObserver("log.txt")
console_obs = ConsoleObserver()

sys = System()

sys.subscribe(console_obs)
sys.subscribe(file_obs)

sys.state = "Activo"
sys.state = "Inactivo"




