from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, sender: str, message: str):
        pass

class NotificationSMS(Notification):
    def send(self, sender: str, message: str):
        print(f"Se envia el mensaje a {sender}: {message}")


class NotificationEmail():
    def send(self, email: str, subject: str, message: str):
        print(f"Se envia el mensaje a {email}: {message}, asunto {subject}")

class NotificationEmailAdapter(Notification):
    def __init__(self, notif_email: NotificationEmail, subject: str):
        self.__notif_email = notif_email
        self.__subject = subject

    def send(self, sender: str, message: str):
        self.__notif_email.send(sender, self.__subject, message)


def create_order(notif: Notification, sender: str, message: str):
    print("Se crea la orden")
    print("Se factura")
    notif.send(sender,message)

notif_sms = NotificationSMS()

create_order(notif_sms,"+6642259769", "Ahi vienen los zetas")

notif_email = NotificationEmail()
notif_email_adapt = NotificationEmailAdapter(notif_email, "Aviso")

create_order(notif_email_adapt,"juan@gmail.com", "No has pagado lol")
