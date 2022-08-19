numbers = input().split(", ")
numbers_list = list(map(int, numbers))  #така с МАР обърнаж всички он стринга в числа-доста по лесно и бързо
even_index_list = []

for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        even_index_list.append(i)

print(even_index_list)
