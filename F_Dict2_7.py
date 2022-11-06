n = int(input())
parking = {}

for _ in range(n):
    data = input().split(" ")
    command = data[0]
    user = data[1]

    if command == "register":
        car_number = data[2]
        if user not in parking.keys():
            parking[user] = car_number
            print(f"{user} registered {car_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_number}")

    elif command == "unregister":
        if user in parking:
            print(f"{user} unregistered successfully")
            del parking[user]
        else:
            print(f'ERROR: user {user} not found')

for keys, value in parking.items():
    print(f'{keys} => {value}')