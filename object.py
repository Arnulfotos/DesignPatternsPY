class People:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def hi(self):
        print("Hola " + self.name)

    def getAge(self):
        return self.__age

    def some(self):
        print("Algo")

    @staticmethod
    def helloworld():
        print("Hola mundo")

    @classmethod
    def helloworld2(cls): # Recuerda que cls es por que ppuede acceder a los atributos de la instancia
        print("Hola mundo2")



class Barman(People):
    pass

    def welcome(self):
        print("Bienvenido")


class Student(People):
    def __init__(self, name, age, profesion):
        super().__init__(name,age)
        self.profesion = profesion

    def hi(self):
        print("Hola soy "+ self.name + "y soy " + self.profesion)


def show(people):
    people.hi()

juan = People("People")

arnulfo = Barman("Arnulfo", 28)
arnulfo.welcome()
cielo = Student("Cielo", 30, "Estudiante frances")
cielo.hi()


