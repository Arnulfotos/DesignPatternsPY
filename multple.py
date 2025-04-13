class SMS:
    def send(self):
        print("Se envia mensaje por SMS")

class Saver:
    def save(self):
        print("Se guarda en bd")

class Email:
    def send(self):
        print("Se envia mail")

class Sale(SMS, Saver, Email):
    pass

sale = Sale()
sale.send()
sale.save()