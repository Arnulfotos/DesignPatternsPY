from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Beer(Prototype):
    def __init__(self, nombre, marca, sizes):
        self.name = nombre
        self.marca = marca
        self.sizes = sizes

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Nombre {self.name}, marca {self.marca}, tamanios {self.sizes}"

beer = Beer("Pikantus", "Erdinger",[1000,500])
print(beer)
beer2 = beer.clone()
beer2.name ="Lupulosa"
beer2.sizes.append(350)


print(beer)
print(beer2)