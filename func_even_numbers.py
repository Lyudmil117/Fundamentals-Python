def even():
    filtered = filter(lambda num: num % 2 == 0, list1)
    print(list(filtered))


list1 = input().split(' ')
list1 = list(map(int, list1))

even()

