from abc import ABC, abstractmethod

class Account:
    def __init__(self, balance: float):
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        print(f"Se ha depositdo: ${amount}, Nuevo saldo: ${self.__balance}")

    def withdraw(self, amount:float):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Se ha retirado: ${amount}, Nuevo saldo: ${self.__balance}")
        else:
            print("Saldo insuficiente")



class Command(ABC):
    def  __init__(self, account: Account):
        self._account = account

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class DepositCommand(Command):
    def __init__(self, account: Account, amount: float):
        super().__init__(account)
        self.__amount = amount

    def execute(self):
        self._account.deposit(self.__amount)

    def undo(self):
        self._account.withdraw(self.__amount)



class WithdrawCommand(Command):
    def __init__(self, account: Account, amount: float):
        super().__init__(account)
        self.__amount = amount

    def execute(self):
        self._account.withdraw(self.__amount)

    def undo(self):
        self._account.deposit(self.__amount)



class TransactionManager:
    def __init__(self):
        self.__commands = []

    def execute_command(self, command: Command):
        command.execute()
        self.__commands.append(command)

    def undo_command(self):
       if self.__commands:
           print("Se ha revertido tu ultimo movimiento")
           command = self.__commands.pop()
           command.undo()
       else:
           print("No hay comandos")

account = Account(100)

trans_manager = TransactionManager()

deposit_command_200 = DepositCommand(account,200)
withdraw_command_100 = WithdrawCommand(account,100)


trans_manager.execute_command(deposit_command_200)
trans_manager.execute_command(deposit_command_200)
trans_manager.execute_command(withdraw_command_100)
trans_manager.undo_command()