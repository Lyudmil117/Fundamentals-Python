text = input()
text1 = []
vowels = ["a", "o", "u", "e", "i"]

for word in text:
    text1.append(word)

for word in text1:
    for vowel in vowels:
        if word.lower() == vowel:
            text1.remove(word)

print("".join(text1))
