numbers = input().split(" ")


def min_max_sum():
    list_numbers = []
    min_number = 0
    max_number = 0
    sum_numbers = 0
    for num in numbers:
        num = int(num)
        list_numbers.append(num)
        min_number = min(list_numbers)
        max_number = max(list_numbers)
        sum_numbers = sum(list_numbers)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_numbers}")


min_max_sum()