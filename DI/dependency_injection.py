from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass




class EmailNotification(Notification):
    def __init__(self, user, pwd, url, port):
        self._user = user
        self._pwd = pwd
        self._url = url


    def send(self,message):
        print(f"Enviando correo electronico: {message}")

class SMSNotification(Notification):
    def __init__(self, user, pwd):
        self._user = user
        self._pwd = pwd
    def send(self,message):
        print(f"Enviando SMS: {message}")

class NotificationManager:
    def __init__(self,notification: Notification):
        self._notification = notification

    def notify(self,message):
        self._notification.send(message)

email = EmailNotification("user","pwd","smtp.azure.com",8899)

notif_man = NotificationManager(email)
notif_man.notify("Mensaje")