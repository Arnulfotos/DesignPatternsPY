class People:

    classname = "people"

    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def hi(self):
            print("Hola " + self.name)

    def getAge(self):
        return self.__age


    @staticmethod
    def helloworld():
        print("Hola mundo")

    @classmethod
    def helloworld2(cls):
        print("Hola mundo2")

arnulfo = People("Cielo",30)
arnulfo.hi()

print(arnulfo.getAge())