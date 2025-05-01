class Memento: #Este es el snapshot
    def __init__(self, state):
        self.__state = state

    @property
    def state(self):
        return self.__state

class Caretaker: # este objeto hace retrive de los objetos solicitados
    def __init__(self):
        self.__history = []

    def save(self, memento):
        self.__history.append(memento)

    def undo(self):
        if len(self.__history) > 1:
            self.__history.pop()
            return self.__history[-1]
        elif len(self.__history) == 1:
            self.__history.pop()
            return None
        else:
            return  None

class Originator: # Este objeto solicita los al caretaker los snapshots y los pone en su respectivo repositorio
    def __init__(self):
        self.__text = ""

    def append(self, new_text):
        self.__text += new_text

    def save(self):
        return Memento(self.__text)

    def restore(self, memento: Memento):
        if memento:
            self.__text = memento.state
        else:
            self.__text = ""

    @property
    def text(self):
        return self.__text


editor = Originator()
historic = Caretaker()

editor.append("Hola! ")
historic.save(editor.save())

editor.append("Soy Arnulfo! ")
historic.save(editor.save())

editor.append("Me gusta programar en C! ")
historic.save(editor.save())

print(f"Editor: {editor.text}")

editor.restore(historic.undo())

print(f"Editor: {editor.text}")

editor.restore(historic.undo())

print(f"Editor: {editor.text}")
