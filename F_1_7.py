num = int(input())

for x in range(num + 1):
    for y in range(x):
        print('*', end='')
    print()

for x in range(num - 1, -1, -1):
    for y in range(x):
        print('*', end='')
    print()

# да отпецхатам пирамида от звездички. Раздели я на две части-примерно върха да е 4ти ред, а след това да почнат
# да намаляват, затова и вадим от NUM-1 и почваме да броим обратно