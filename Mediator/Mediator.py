from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify (self, event: str):
        pass


class BaseComponent(ABC):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator

class ComponentA(BaseComponent):
    def hi(self):
        print("Hola soy A")
        self._mediator.notify("A")

    def response(self):
        print("Que tal! soy A")


class ComponentB(BaseComponent):
    def hi(self):
        print("Hola soy B")
        self._mediator.notify("B")

    def response(self):
        print("Que tal! soy B")


class ConcreteMediator(Mediator):
    def __init__(self, compA: BaseComponent, compB: BaseComponent):
        self._compA = compA
        self._compB = compB
        self._compA.set_mediator(self)
        self._compB.set_mediator(self)

    def notify(self, event: str):
        if event == "A":
            self._compB.response()
        elif event == "B":
            self._compA.response()


comp_a = ComponentA()
comp_b = ComponentB()

mediator = ConcreteMediator(comp_a,comp_b)
comp_a.hi()
comp_b.hi()
