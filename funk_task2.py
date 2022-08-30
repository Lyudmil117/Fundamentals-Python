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


#better way(shown by the tutor)

def sum_numbers(a, b):
    return a + b

def subtract(current_sum, c):
    return current_sum - c

a, b, c = int(input()), int(input()), int(input())
result = subtract(sum_numbers(a, b), c)  #here instead of a,b,c | sum_numbers(a,b) is basicaly = current sum |
