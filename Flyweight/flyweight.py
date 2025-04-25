from abc import ABC, abstractmethod

class Flyweight(ABC):
    def print(self, size: int):
        pass

class ConcreteFlyweight(Flyweight):
    def __init__(self, character: str):#character is state
        self.__character = character # intrinseco o compartido

    def print(self, size: int):
        print(f"Letra {self.__character} con tamanio {size}")# size: estado no compartido


class FlyweightFactory:
    def __init__(self):
        self.__characters = {}

    def get(self, character: str) -> Flyweight:
        if character not in self.__characters:
            print(f"Se crea {character}")
            self.__characters[character] = ConcreteFlyweight(character)

        return self.__characters[character]

flyweight_factory = FlyweightFactory()

a1 = flyweight_factory.get("a")
a1.print(11)
a2 = flyweight_factory.get("a")
a2.print(12)

a3 = flyweight_factory.get("a")
a3.print(15)

b1 = flyweight_factory.get("b")
b1.print(40)


