import math
from math import ceil

num_pers = int(input())
capacity = int(input())

courses = num_pers / capacity
courses = math.ceil(courses)


print(courses)