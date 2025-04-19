from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass

class LocalTaxStrategy(TaxCalculator):
    def calculate(self, amount: float) -> float:
        return amount * 0.16

class ForeignTaxStrategy(TaxCalculator):
    def calculate(self, amount: float) -> float:
        return amount * 0.50


class AbstractSale(ABC):
    def __init__(self,tax_calc: TaxCalculator, concepts):
        self.tax_calc = tax_calc
        self.concepts = concepts

    @abstractmethod
    def calc_total(self):
        pass

class Sale(AbstractSale):
    def calc_total(self):
        total = sum(self.concepts)
        return total + self.tax_calc.calculate(total)


sale = Sale(LocalTaxStrategy(), [100,200,300])
print(sale.calc_total())
sale2 = Sale(ForeignTaxStrategy(), [100,200,300])
print(sale2.calc_total())

# Take a remote. The remote has buttons 1-6. This is the concrete class in the diagram above. Each button will work different depending on if the remote is used for a TV or DVD. The functionality for each button is abstracted from the implementation by the implementer interface.