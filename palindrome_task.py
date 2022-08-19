words_list = input().split(", ")
list = []
palindrome = input()
list2 = []

for word in words_list:
    if word == palindrome:
        list.append(word)
    rev_word = reversed(word)
    rev_word = "".join(rev_word)
    if word == rev_word:
        list2.append(word)

print(list2)
print(list.count(palindrome))
