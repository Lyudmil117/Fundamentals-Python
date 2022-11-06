command = input()
phone_book = {}
while not command.isdigit():
    numbers = command.split("-")
    person = numbers[0]
    phone_num = numbers[1]
    phone_book[person] = phone_num

    command = input()

for _ in range(int(command)):
    name = input()
    if name in phone_book.keys():
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')


