from itertools import count


def show(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} {value}")

show(name ="Arnulfo", country = "Mexico")
