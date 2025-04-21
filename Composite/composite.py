from abc import ABC, abstractmethod

class FileComponent(ABC):
    @abstractmethod
    def show(self, space=0):
        pass

class FileLeaf(FileComponent):
    def __init__(self, name):
        self.__name = name

    def show(self, space = 0):
        print(" " * space + f"- Archivo {self.__name}")



class FolderComposite(FileComponent):
    def __init__(self, name):
        self.__name = name
        self.__children = []

    def add(self, component: FileComponent):
        self.__children.append(component)

    def remove(self, component: FileComponent):
        self.__children.remove(component)

    def show(self, space = 0):
        print(" " * space + f"+ Carpeta: {self.__name}")
        for child in self.__children:
            child.show(space + 2)



archivo1 = FileLeaf("text1.txt")
archivo2 = FileLeaf("text2.txt")
archivo3 = FileLeaf("text3.txt")

root = FolderComposite("root")
folder1 = FolderComposite("Folder1")

root.add(folder1)
folder1.add(archivo1)
folder1.add(archivo2)
folder1.add(archivo3)

root.show()

# Jeraquias de elementos que estan compuestos de otro elementos
#

#You may find it being-a-must when you will be working with binary trees or other complex data structures like list of lists of lists - etc... then, when every element (class) implements 1 interface, you can do the same methods on 1 leaf or on whole group of them - copping, adding, removing, moving... whatever, what you have implemented correctly. It's very useful and simple.
