words = input().split()
string1 = ""
for word in words:
    string1 += (word * len(word))

print(string1)
