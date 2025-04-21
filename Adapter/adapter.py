from abc import ABC, abstractmethod

class Target(ABC):
    @abstractmethod
    def payment(self, amount: float):
        pass


class Adaptee:
    def __init__(self):
        self.__contected = False

    def connect(self):
        print("Conectando con API")
        self.__contected = True

    def pay(self, amount: float):
        if self.__contected:
            print(f"Realizamos el pago por {amount}")


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.__adaptee = adaptee

    def payment(self, amount: float):
        self.__adaptee.connect()
        self.__adaptee.pay(amount)


def create_order(pay: Target, amount: float):
    pay.payment(amount)
    print(f"Se factura")
    print(f"Se envia factura por email")

adaptee = Adaptee()
adapter = Adapter(adaptee)

create_order(adapter,15)