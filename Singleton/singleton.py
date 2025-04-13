class Singleton:
    _instance = None # None es equivalente a null
    def __new__(cls, name = None, age = None):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.name = name
            cls._instance.age = age
        return cls._instance


singleton1 = Singleton("Hector", 30)
singleton2 = Singleton("Arnulfo", 20)

print(singleton2.name)
# __new__ este es el encargado de construir el objeto, se ejecuta
# antes que el __init___

# __protected es simbolico

