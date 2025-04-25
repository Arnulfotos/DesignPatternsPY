from abc import ABC,abstractmethod

class Handler(ABC):
    def __init__(self, issues, next: 'Handler' = None):
        self._issues = issues
        self._next = next

    @abstractmethod
    def handle(self,issue):
        pass

class Level1Support(Handler):
    def handle(self,issue):
        if issue in self._issues:
            print(f"Nivel 1: Resolviendo {issue}")
        elif self._next:
            print("Nivel 1: Escalando problema al siguiente nivel")
            self._next.handle(issue)


class Level2Support(Handler):
    def handle(self, issue):
        if issue in self._issues:
            print(f"Nivel 2: Resolviendo {issue}")
        elif self._next:
            print("Nivel 2: Escalando problema al siguiente nivel")
            self._next.handle(issue)

class Level3Support(Handler):
    def handle(self, issue):
        if issue in self._issues:
            print(f"Nivel 3: Resolviendo {issue}")
        elif self._next:
            print("Nivel 3: Escalando problema al siguiente nivel")
            self._next.handle(issue)


class SupportManager(Handler):
    def handle(self, issue):
        print(f"Gerente de soporte: Resolviendo {issue}")


manager = SupportManager([])
lvl3 = Level3Support(["database_crash","production_down"],manager)
lvl2 = Level2Support(["bug","user_deleted","exception"],lvl3)
lvl1 = Level1Support(["password_reset","user_create"], lvl2)

lvl1.handle("database_crash")
