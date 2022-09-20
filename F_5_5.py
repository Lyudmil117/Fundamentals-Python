n = int(input())
list1 =[]
wanted = []

for i in range(n):
    number = int(input())

    if command == "even":
        if number % 2 == 0:
            list1.append(number)
    elif command == "odd":
        if number % 2 != 0:
            list1.append(number)
    elif command == "positive":
        if number >= 0:
            list1.append(number)
    elif command == "negative":
        if number < 0:
            list1.append(number)


