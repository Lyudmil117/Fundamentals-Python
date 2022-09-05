text = input()

letters = ""
digits = ""
symbools = ""

for char in text:
    if char.isdigit(): #if char is digit in text
        digits += char
    elif char.lower() or char.upper(): # if char is lower case or upper IT IS A LETTER
        letters += char
    else:
        symbools += char #if it is not a digit ot letter it is symbol

print(letters)
print(digits)
print(symbools)