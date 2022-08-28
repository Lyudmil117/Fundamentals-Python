def small():
    list1 = []
    for num in range(3):
        num = int(input())
        list1.append(num)
    small_num = min(list1)
    print(small_num)


small()
