banned = input().split("")
text = input()

for word in text:
    while word in banned:
        text = text.replace(word, "*" * len(word))
# until there is word in Text(form the banned words), replace it with ** with the same leght of the banned word

print(text)