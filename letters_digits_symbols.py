text = input()

letters = ""
digits = ""
symbools = ""

for char in text:
    if char.isdigit(): #if char is digit in text
        digits += char
    elif char.lower() or char.upper(): # if char is lower case or upper IT IS A LETTER
        letters += char                    #here we can use alse method ISAPLPHA() ,to check if it is a letter
    else:
        symbools += char #if it is not a digit ot letter it is symbol

print(letters)
print(digits)
print(symbools)


#we can do it also like that:

for char in text:
    if char.isalnum():      #if char is letter or digit
        if char.isalpha():
            letters += char
        else:
            digits += char
    else:
        symbools += char
