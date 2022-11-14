n = int(input())
garage = {}

for _ in range(n):
    car_data = input().split("|")
    car = car_data[0]
    mileage = int(car_data[1])
    fuel = int((car_data[2]))
    garage[car] = [mileage, fuel]

commands = input()

while commands != "Stop":
    data = commands.split(" : ")
    action = data[0]
    car = data[1]

    if action == "Drive":
        distance_to_drive = int(data[2])
        fuel_to_drive = int(data[3])

        if garage[car][1] < fuel_to_drive:
            print('Not enough fuel to make that ride')
        else:
            garage[car][0] += distance_to_drive
            garage[car][1] -= fuel_to_drive
            print(f"{car} driven for {distance_to_drive} kilometers. {fuel_to_drive} liters of fuel consumed.")

        if garage[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            garage.pop(car)

    elif action == "Refuel":
        extra_fuel = int(data[2])

        if garage[car][1] + extra_fuel > 75:
            difference = 75 - garage[car][1]
            garage[car][1] = 75
        else:
            garage[car][1] += extra_fuel
            difference = extra_fuel

        print(f"{car} refueled with {difference} liters")

    elif action == "Revert":
        kilometers = int(data[2])
        if garage[car][0] - kilometers > 10000:
            garage[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            garage[car][0] = 10000

    commands = input()

for car in garage:
    print(f'{car} -> Mileage: {garage[car][0]} kms, Fuel in the tank: {garage[car][1]} lt.')
