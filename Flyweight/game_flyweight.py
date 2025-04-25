from abc import ABC, abstractmethod

class TypeCar(ABC):
    @abstractmethod
    def print(selfself,x,y):
        pass

class TyperCarCommon(TypeCar):
    def __init__(self,name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def print(self,x,y):
        print(f"Auto {self.name} de color {self.color} y modelo {self.model} en posicion ({x},{y})")


class CarFactory:
    def __init__(self):
        self.__types_Car = {}

    def get(self,name,color,model) -> TypeCar:
        key = (name,color, model)
        if key not in self.__types_Car:
            print(f"Se ha creado el carro {name} {color} {model}")
            self.__types_Car[key] = TyperCarCommon(name, color, model)

        return self.__types_Car[key]


class Car:
    def __init__(self, x, y, type_car: TypeCar):
        self.x = x
        self.y = y
        self.__type_car = type_car

    def print(self):
        self.__type_car.print(self.x, self.y)


class Game:
    def __init__(self):
        self.__Cars =[]
        self.__Car_factory = CarFactory()
    def add_car(self,x,y,name,color,model):
        type_car = self.__Car_factory.get(name,color,model)
        car = Car(x,y,type_car)
        self.__Cars.append(car)

    def print(self):
        for car in self.__Cars:
            car.print()



game = Game()
game.add_car(10, 15, "Nissan", "Rojo", "2022")
game.add_car(25, 30, "Nissan", "Rojo", "2022")  # Usará el mismo objeto TyperCarCommon
game.add_car(40, 45, "Toyota", "Blanco", "2021")
game.add_car(80, 70, "Toyota", "Blanco", "2021")

game.add_car(5, 10, "Ford", "Azul", "2020")

# Imprimir todos los autos
game.print()