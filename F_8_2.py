def add():
    return x1 + x2


def subtract():
    return (x1 + x2) - x3


def add_and_subtract():
    print(add())
    print(subtract())


x1 = int(input())
x2 = int(input())
x3 = int(input())
print(subtract())

