def abs_calc():
    list1 = input().split(" ")
    list2 = []
    for number in list1:
        list2.append(abs(float(number)))
    print(list2)

abs_calc()