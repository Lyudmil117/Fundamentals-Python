def calculator():
    max_number = max(list1)
    min_number = min(list1)
    sum_list_numbers = sum(list1)
    print(f'The minimum number is : {min_number}')
    print(f'The maximum number is: {max_number}')
    print(f'The sum of all numbers is: {sum_list_numbers}')


list1 = input().split(' ')
list1 = list(map(int, list1))
calculator()