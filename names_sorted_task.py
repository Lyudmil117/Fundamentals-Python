names = input().split(", ")
alphabet_sorted = sorted(names)
#сега ще ги сортираме и по дължина на името. Е така се прави по-долу. Така се брои отзад напред -len(nesrto))
sorted_by_alphabet_and_lenght = sorted(alphabet_sorted, key=lambda nesto: -len(nesto))

print(sorted_by_alphabet_and_lenght)