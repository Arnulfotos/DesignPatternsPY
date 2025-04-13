from abc import ABC, abstractmethod
class Taco(ABC): #Interfaz
    @abstractmethod
    def price(self):
        pass
    @abstractmethod
    def description(self):
        pass


class BasicTaco(Taco): #Concrete component
    def price(self):
        return 5
    def description(self):
        return "Taco "



class TacoDecorator(Taco):
    def __init__(self, taco: Taco):
        self._taco = taco #1 guion bajo es protected

    def price(self):
        return self._taco.price()

    def description(self): ## especial a utilizar con super()
        return self._taco.description() + "extra "


class DoubleMeatTaco(TacoDecorator):
    def price(self):
        return self._taco.price() + 4

    def description(self):
        return super().description() + "Doble carne "


class CheeseTaco(TacoDecorator):
    def price(self):
        return self._taco.price() + 2
    def description(self):
        return super().description() + "Queso "


taco = BasicTaco()

print(f"{taco.description()}{taco.price()}")

double_meat_taco =  DoubleMeatTaco(taco)

print(f"{double_meat_taco.description()}{double_meat_taco.price()}")

cheese_taco = CheeseTaco(double_meat_taco)

print(f"{cheese_taco.description()}{cheese_taco.price()}")