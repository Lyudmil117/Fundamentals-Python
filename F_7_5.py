def order():
    product = input()
    quantity = int(input())
    total = 0
    if product == "coffee":
        total = quantity * 1.50
    elif product == "water":
        total = quantity * 1.00
    elif product == "coke":
        total = quantity * 1.40
    elif product == "snacks":
        total = quantity * 2.00

    print(f'{total:.2f}')


order()