from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    @abstractmethod
    def calculate(self,amount: float) -> float:
        pass


class IVAStrategy(TaxStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.16

class IRSStrategy(TaxStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.30

class TaxCalculator:
    def __init__(self, strategy: TaxStrategy):
        self.__strategy = strategy
    def set_strategy(self, strategy: TaxStrategy):
        self.__strategy = strategy
    def calculate(self, amounts: list[float])-> list[float]:
        taxes =[]

        for amount in amounts:
            taxes.append(self.__strategy.calculate(amount))
        return taxes

amounts = [100,30,18]

iva_strg = IVAStrategy()
isr_strg = IRSStrategy()

tax_calc = TaxCalculator(iva_strg)

print(tax_calc.calculate(amounts))