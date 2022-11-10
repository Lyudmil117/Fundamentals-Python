word = input()
string1 = input()

while word in string1:
    string1 = string1.replace(word, "")

print(string1)