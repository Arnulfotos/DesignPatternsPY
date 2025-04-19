from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def pay(self, order):
        pass
    @abstractmethod
    def ship(self, order):
        pass
    @abstractmethod
    def deliver(self, order):
        pass

class NewOrderState(OrderState):
    def pay(self, order):
        print("El peddido se ha pagado con exito")
        order.set_state(PaidOrderState())

    def ship(self, order):
        print("No se puede enviar sin estar pagado")

    def deliver(self, order):
        print("No se entregar enviar sin estar pagado")


class PaidOrderState(OrderState):
    def pay(self, order):
        print("El peddido ya se ha pagado")


    def ship(self, order):
        print("Enviado con exito")
        order.set_state(ShippedOrderState())

    def deliver(self, order):
        print("No se entregar entregar sin estar enviado")

class ShippedOrderState(OrderState):
    def pay(self, order):
        print("El peddido ya se ha pagado")

    def ship(self, order):
        print("El pedido ha sido enviado")


    def deliver(self, order):
        print("Entrega finalizada")
        order.set_state(FinishedOrderState())


class FinishedOrderState(OrderState):
    def pay(self, order):
        print("El peddido ya se entrego")

    def ship(self, order):
        print("El pedido ya se entrego")

    def deliver(self, order):
        print("El pedido ha sido entregado")


class Order:
    def __init__(self, state: OrderState):
        self.state = state

    def set_state(self,state: OrderState):
        self.state = state

    def pay(self):
        self.state.pay(self)

    def ship(self):
        self.state.ship(self)

    def deliver(self):
        self.state.deliver(self)


# vas manejando situaciones con los objetos
# Tienes que definir los states y un objeto central el cual es el que accionala lo requerido segun el objeto en el momento
# Evitar comportamientos inesperados
# Hacer un encadenamiento de estados
# Hay soluciones requiere navegar entre estados, como un semaforo


order = Order(NewOrderState())
order.ship()
order.deliver()
order.pay()
order.deliver()
order.pay()
order.ship()
order.deliver()
order.ship()