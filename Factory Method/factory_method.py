from abc import ABC, abstractmethod

class Concept(ABC): #product interface
    @abstractmethod
    def description(self) -> str:
        pass
    @abstractmethod
    def price(self) -> float:
        pass

class Product(Concept):

    def __init__(self, amount, tax):
        self.__amount = amount
        self.__tax = tax

    def description(self) -> str:
        return "Producto"

    def price(self) -> float:
        return self.__amount + self.__tax

class Servicio(Concept):

    def __init__(self, amount):
        self.__amount = amount

    def price(self) -> float:
        return self.__amount


    def description(self) -> str:
        return "Servicio"


class ConceptFactory(ABC):
    def __init__(self, *args): #Aqui obligamos a que se utilicen paramtros para consturir los objetos
        self._args = args

    @abstractmethod
    def create(self) -> Concept:
        pass



class ProductFactory(ConceptFactory):
    def create(self) -> Concept:
        return Product(self._args[0], self._args[1])

class ServiceFactory(ConceptFactory):
    def create(self) -> Concept:
        return Servicio(self._args[0])


def show_info(concept: Concept):
    print(f"el concepto es un {concept.description()}")

p_f = ProductFactory(12,2)
s_f = ServiceFactory(20)

concept1 = p_f.create()
concept2 = s_f.create()

show_info(concept1)
show_info(concept2)
print(concept1.price())
print(concept2.price())