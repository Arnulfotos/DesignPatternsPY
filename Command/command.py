from abc import ABC, abstractmethod

class Receiver:
    def open(self):
        print("Se abre documento")
    def save(self, file_name):
        print(f"Se guarda documento en {file_name}")
    def print(self):
        print("Se imprime doc")

class Command(ABC):
    def __init__(self, receiver: Receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass

class OpenCommand(Command):
    def execute(self):
        self._receiver.open()

class SaveCommand(Command):
    def __init__(self,receiver : Receiver, file_name):
        super().__init__(receiver)
        self.__file_name = file_name
    def execute(self):
        self._receiver.save(self.__file_name)

class PrintCommand(Command):
    def execute(self):
        self._receiver.print()

# Separas acciones

class Invoker:
    def __init__(self, open: Command, save: Command, print: Command):
       self.open = open
       self.save = save
       self.print = print

    def click_open(self):
        self.open.execute()

    def click_save(self):
        self.save.execute()

    def click_print(self):
        self.print.execute()

receiver = Receiver()
open_comm = OpenCommand(receiver)
save_comm = SaveCommand(receiver,"document.txt")
print_command = PrintCommand(receiver)

inv = Invoker(open_comm,save_comm,print_command)

inv.click_open()
inv.click_save()
inv.click_print()

