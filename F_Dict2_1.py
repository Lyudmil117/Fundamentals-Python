dict = {}
word = input()

for char in word:
    if char not in dict and char != " ": # проверяваме дали я има в речника и дали не е " "
        dict[char] = 1                     #ако я няма я създаваме

    else:
        dict[char] += 1                 #ако я има я добавяме

for key,value in dict.items():
    print(f'{key} -> {value}')

#  ДРУГ НАЧИН!!!

from collections import Counter

word = input()
result = Counter(word)
print(result)              # pak dava sustiq rezultat { t:2, e; 1:, x:1} na dumata TEXT

for key, value in result.items():
    if key != " ":
        print(f'{key} -> {value}')
