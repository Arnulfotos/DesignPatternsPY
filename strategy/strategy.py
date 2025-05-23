from abc import ABC,abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self,a,b):
        pass

class AddStrategy(Strategy):
    def execute(self,a,b):
        return a + b

class MulStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class Operation:
    def __init__(self, strategy: Strategy):
        self.__strategy = strategy

    def calculate(self,a,b):
        return self.__strategy.execute(a,b)

    def set_strategy(self, strategy: Strategy):
        self.__strategy = strategy



add_strategy = AddStrategy()
mul_Strategy = MulStrategy()
operation = Operation(add_strategy)

print(operation.calculate(5,7))
operation.set_strategy(mul_Strategy)
print(operation.calculate(5,7))