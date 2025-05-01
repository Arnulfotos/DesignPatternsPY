from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, message: str, sender: object):
        pass

class ChatMediator(Mediator):
    def __init__(self,log):
        self._users = []
        self._log = log
        self._log.set_mediator(self)

    def add_user(self,user):
        self._users.append(user)

    def notify(self, message: str, sender: object):
        self._log.recive(message)
        for user in self._users:
            if user != sender:
                user.recive(message)

class User:
    def __init__(self, name: str, mediator: Mediator):
        self._name = name
        self._mediator = mediator
        mediator.add_user(self)

    def send(self, message: str):
        print(f"{self._name} envia: {message}")
        self._mediator.notify(message, self)

    def recive(self, message: str):
        print(f"{self._name} recibe: {message}")


class Log:
    def __init__(self, log_file:str):
        self.__log_file = log_file
        self._mediator = None

    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator

    def send(self, msg: str):
        print(f"El log envia: {msg}")
        self._mediator.notify(msg,self)

    def recive(self, msg: str):
        with open(self.__log_file,"a") as file:
            file.write(msg + "\n")

log = Log("log.txt")
ChatMediator = ChatMediator(log)
Juan = User("Juan", ChatMediator)
Arnulfo = User("Arnulfo", ChatMediator)
Cielo = User("Cielo", ChatMediator)


Juan.send("Hola a todos")
Cielo.send("Hola!!!!")

log.send("Se ha ido la conexion")