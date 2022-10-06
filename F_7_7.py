
def rounder():
    lst1 = input().split(" ")
    lst2 = []
    for item in lst1:
        item = float(item)
        lst2.append(round(item))
    print(lst2)


rounder()