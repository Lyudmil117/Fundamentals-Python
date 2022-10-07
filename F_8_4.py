def odd_even():
  
    odd_sum = 0
    even_sum = 0
    number = input()
    for num in number:
        num_list.append(int(num))
    for x in num_list:
        if x % 2 == 0:
            even_sum += x
        else:
            odd_sum += x
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


odd_even()
