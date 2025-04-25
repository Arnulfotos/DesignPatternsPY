from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, next: 'Handler' = None):
        self._next = next

    @abstractmethod
    def handle(self, request):
        pass

class ConcreteHandlerA(Handler):
    def handle(self,request):
        if request == "A":
            print("Se ejectua A")
        elif self._next:
            print("Se pasa al siguiente")
            self._next.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Se ejectua B")
        elif self._next:
            print("Se pasa al siguiente")
            self._next.handle(request)


class ConcreteHandlerDefault(Handler):
    def handle(self, request):
            print("Se ejectua el default")

default = ConcreteHandlerDefault()
concreteB = ConcreteHandlerB(default)
chain = ConcreteHandlerA(concreteB)

chain.handle("zxvxzvB")


