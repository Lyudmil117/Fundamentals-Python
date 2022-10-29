words = input().split(" ")
words_lower = list(map(lambda w: w.lower(), words)) # use LAMBDA F to make all words lowercase in list WORDS

occurrences = {}

for word in words_lower:
    if word not in occurrences:
        occurrences[word] = 1    # ako няма думата в речника я създай
    else:
        occurrences[word] += 1   # ако има WORD в occurrences просто я добави

for key, value in occurrences.items():
    if value % 2 != 0:        # ако думата я има нечетен брой пъти в речника я отпечатай на един ред
        print(key, end=" ")

