class Stock:
    def check(selfself, concepts) -> bool:
        return True

class Payment:
    def pay(self, customer_id, concepts):
        print(f"Se realiza pago")

class Email:
    def send(self, customer_id):
        print(f"Su compra fue hecha con exito")




class Facade:
    def __init__(self):
        self.__stock = Stock()
        self.__payment = Payment()
        self.__email = Email()

    def create_payment(self, concepts, customer_id):
        if self.__stock.check(concepts):
            self.__payment.pay(customer_id, concepts)
            self.__email.send(customer_id)



concepts = [{"id": 1, "quantity":10},{"id": 2, "quantity":20},{"id": 3, "quantity":30}]

facade = Facade()

facade.create_payment(concepts,1)