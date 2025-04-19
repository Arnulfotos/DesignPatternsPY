from abc import ABC, abstractmethod
# Vas creando un objeto con otro objetos, con setters de otro objeto
class People:
    def __init__(self):
        self.name = None
        self.age = None
        self.country = None
        self.weight = None

    def __str__(self):
        return f"Nombre: {self.name}, Edad {self.age}"

class Builder(ABC):
    @abstractmethod
    def set_name(self, name):
        pass
    @abstractmethod
    def set_age(self, age):
        pass
    @abstractmethod
    def set_country(self, country):
        pass
    @abstractmethod
    def set_weight(self, weight):
        pass

class PeopleBuilder(Builder):
    def __init__(self):
        self.__people = People()


    def set_name(self, name):
        self.__people.name = name
        return self

    def set_age(self, age):
        self.__people.age = age
        return self

    def set_country(self, country):
        self.__people.country = country
        return self

    def set_weight(self, weight):
        self.__people.weight = weight
        return self

    def build(self):
        people = self.__people
        self.reset()
        return people

    def reset(self):
        self.__people = People()

class PeopleDirector:
    def __init__(self,builder: Builder):
        self.builder = builder

    def create_arnulfo(self):
        self.builder.set_name("Arnulfo").set_age(28).set_country("Mexico")
        return self.builder.build()

    def create_cielo(self):
        self.builder.set_name("Cielo").set_age(30).set_country("Mexico").set_weight(50)
        return self.builder.build()

people_builder = PeopleBuilder()

arnulfo = people_builder.set_name("Arnulfo").set_age(28).set_country("Mexico").build()

print(arnulfo)
people_director = PeopleDirector(people_builder)
cielo = people_director.create_cielo()
print(cielo)