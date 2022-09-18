n = int(input())
suma = 0

for x in range(n):
    letter = input()
    number = ord(letter)
    suma += number

print(f'The sum equals: {suma}')
