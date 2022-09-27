n = int(input())

for a in range(n):
    for b in range(n):
        for c in range(n):
            print(f'{chr(a + 97)}{chr(b + 97)}{chr(c + 97)}')

# note the use of ascii table number of the character - 97 + iteration element