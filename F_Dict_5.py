words = input().split(", ")

dict = {word: ord(word) for word in words} #dictionary comprehension
print(dict)

# words = input().split(", ")
# dict = {}
#
# for word in words:
#     dict[word] = ord(word)

# така става без dictionary comprehension
