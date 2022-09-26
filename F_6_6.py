list1 = list(map(int, input().split(" ")))
list2 = []
n = int(input())
minimal = ''
for x in range(1, n + 1):
    minimal = min(list1)
    list1.remove(minimal)
    list2 = ", ".join(map(str, list1))

print(list2)

