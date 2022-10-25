cars_to_be_taxed = input().split(">>")
agency = 0

for car in cars_to_be_taxed:
    current_car = car.split(" ")
    total_tax = 0
    tax = 0
    car_type = current_car[0]
    years = int(current_car[1])
    kilometers = int(current_car[2])

    if car_type == "family":
        initial_tax = 50
        tax = initial_tax - (years * 5)
        total_tax = tax + ((kilometers // 3000) * 12)
    elif car_type == "heavyDuty":
        initial_tax = 80
        tax = initial_tax - (years * 8)
        total_tax = tax + ((kilometers // 9000) * 14)
    elif car_type == "sports":
        initial_tax = 100
        tax = initial_tax - (years * 9)
        total_tax = tax + ((kilometers // 2000) * 18)

    else:
        print("Invalid car type.")
        continue

    agency += total_tax

    print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {agency:.2f} euros in taxes.")