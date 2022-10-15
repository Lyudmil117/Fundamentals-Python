text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = ''
for ch in text:
    if ch.lower() not in vowels:
        result += ch

print(result)