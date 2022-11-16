text = input()
new_text = ""
for char in text:
    if char not in new_text:
        new_text += char

print(new_text)
