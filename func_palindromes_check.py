def palindromes():
    for palin in list1:
        if palin == palin[::-1]:
            print(True)
        else:
            print(False)


list1 = input().split(', ')
palindromes()