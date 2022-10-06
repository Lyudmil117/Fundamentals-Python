def calculator():
    operator = input()
    x = int(input())
    y = int(input())
    if operator == "add":
        print(x + y)
    elif operator == "subtract":
        print(x - y)
    elif operator == "multiply":
        print(x * y)
    elif operator == "divide":
        print(int(x / y))


calculator()
