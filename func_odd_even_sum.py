def odd_even_sum():
    list1 = []
    for char in number:
        list1.append(int(char))

    even = 0
    odd = 0
    for char in list1:
        if char % 2 == 0:
            even += char

        else:
            odd += char

    print(f'Odd sum = {odd}')
    print(f'Even sum = {even}')


number = input()
odd_even_sum()
