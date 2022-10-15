list1 = list(map(int, input().split(", ")))
index_list = [num for num in range(len(list1)) if list1[num] % 2 == 0]
# this is how i can check which are indexes of even numbers

print(index_list)
