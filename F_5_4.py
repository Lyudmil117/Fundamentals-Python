n = int(input())
search_word = input()
list1 = []
list2 = []

for _ in range(n):
    word = input()
    list1.append(word)
print(list1)

for i in range(len(list1) - 1, -1, -1):
    element = list1[i]
    if search_word not in element:
        list1.remove(element)

print(list1) 
