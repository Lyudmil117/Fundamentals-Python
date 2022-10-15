names = input().split(", ")
sorted_list = sorted(names, key=lambda x: (-len(x), x))

print(sorted_list)
#
# # HOW THIS WORKS?
# LIST = [6, 2, 1, 4, 3, 5]
# sorted_nubers = sorted(list, key=lambda x: -x) - this means sort them bigger to smaller number