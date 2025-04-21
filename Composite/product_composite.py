from abc import ABC, abstractmethod

class SaleCompoment(ABC):
    @abstractmethod
    def get_total(self):
        pass
    def details(self,space=0):
        pass


class Product(SaleCompoment):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_total(self):
        return self.__price

    def details(self,space=0):
        print(" " * space + f"- Product: {self.__name}, Price: {self.__price}")

class Package(SaleCompoment):
    def __init__(self,name):
        self.__name = name
        self.__products = []

    def add(self,product: SaleCompoment):
        self.__products.append(product)

    def remove(self, product: SaleCompoment):
        self.__products.remove(product)

    def get_total(self):
        total = 0
        for product in self.__products:
            total += product.get_total()
        return total

    def details(self,space=0):
        print(" " * space + f"+ Paquete: {self.__name}, Total Precio: ${self.get_total()}")
        for product in self.__products:
            product.details(space + 2)


product1 = Product("Stout Cafe de Olla", 7)
product2 = Product("Colimita", 5)

product3 = Product("High Miller", 10)
product4 = Product("Miller Lite", 6)

mx_package = Package("MX Beer")
us_package = Package("USA Beer")


mx_package.add(product1)
mx_package.add(product2)

us_package.add(product3)
us_package.add(product4)

total_Sale = Package("Total Sale")
total_Sale.add(mx_package)
total_Sale.add(us_package)
total_Sale.details()