numbers = input().split(" ")


def sorted_f():
    list1 = []
    for num in numbers:
        num = int(num)
        list1.append(num)
    print(sorted(list1))


sorted_f()