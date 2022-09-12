n = int(input())

for i in range(n):
    string = input()
    if string.__contains__('.') or string.__contains__('_') or string.__contains__(","):
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')

#or

for i in range(n):      #check if in string everyting is letters (isaplpha()), Special chars are not, so it will show
    string = input()
    if string.isalpha():
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
        