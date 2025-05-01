class CharacterMemento:
    def __init__(self, salud, posicion):
        self.__health = salud
        self.__position = posicion

    @property
    def state(self):
        return {"health": self.__health, "position": self.__position}

class Game:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.position = (0,0)

    def move(self,x,y):
        self.position = (x,y)

    def recive_damege(self,damage):
        self.health = self.health - damage

    def save(self):
        return CharacterMemento(self.health, self.position)

    def restore(self, memento):
        if memento:
            state = memento.state
            self.health = state["health"]
            self.position = state["position"]

    def __str__(self):
        return (f"{self.name} - Salud: {self.health} Position: {self.position}")


class CharacterHistory:
    def __init__(self):
        self.__history = []

    def save(self, memento):
        self.__history.append(memento)

    def undo(self):
        if len(self.__history) > 1:
            self.__history.pop()
            return self.__history[-1]
        elif self.__history:
            self.__history.pop()
            return None

        return None

character = Game("Hero")
history = CharacterHistory()

print(f"Estado inicial {character}")
history.save(character.save())

character.move(5,10)
character.recive_damege(20)
history.save(character.save())
print(f"Ahora {character}")

character.move(10,10)
character.recive_damege(20)
history.save(character.save())
print(f"Ahora {character}")

character.restore(history.undo())
print(f"Ahora {character}")

# El caretaker recibe snapshots, el Originator los usa del caretaker para restaurarlos
