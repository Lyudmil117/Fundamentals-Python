list1 = list(map(int, input().split(' ')))
list2 = []

for num in list1:
    if num > 0:
        list2.append(-num)
    elif num <= 0:
        list2.append(abs(num))

print(list2)


