#Intermediario de otro objeto
# Para ahorrar recursos

from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def action(self):
        pass

class RealSubject(Subject):
    def action(self):
        print("Realizar accion")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self.__real_subject = real_subject
        self.__authorized = False

    def action(self):
        if self.__authorized:
            print("Proxy: accesso permitido")
            self.__real_subject.action()
        else:
            print("Proxy: accesso no permitido")

    def log_in(self, user: str, pwd: str):
        if user == "user" and pwd == "123456":
            self.__authorized = True



def some(subject: Subject):
    subject.action()

real_subject = RealSubject()




#some(real_subject)

proxy = Proxy(real_subject)
proxy.log_in("user", "123456")
some(proxy)
