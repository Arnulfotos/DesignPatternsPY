from functools import total_ordering


def add(*args):
    total = 0
    for number in args:
        total += number
    return total

res1 = add(1,2,3)

print(res1)