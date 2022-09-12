num = int(input())
condition = False
for i in range(num):
    number = int(input())
    if number % 2 != 0:
        condition = False
        break

    elif number % 2 == 0:
        condition = True

if condition == True:
    print('All numbers are even.')
else:
    print(f'{number} is odd!')
