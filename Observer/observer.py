from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def refresh(self, ticket_number):
        pass


class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
        self._tickets = 1

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
            observer.refresh(self._tickets)

    def sell(self):
        self.notify()
        self._tickets +=1

class sendMail(Observer):
    def refresh(self, ticket_number):
        print(f"Se envia un correo al gerente: {ticket_number}")

class Invoice(Observer):
    def refresh(self, ticket_number):
        print(f"Se envia factura al cliente: {ticket_number}")


send_mail = sendMail()
invoice = Invoice()

SUBJECT = Subject()

SUBJECT.subscribe(send_mail)
SUBJECT.subscribe(invoice)

SUBJECT.sell()