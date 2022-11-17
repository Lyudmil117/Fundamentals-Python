tour_stops = input()
command = input()

while command != "Travel":
    data = command.split(":")
    action = data[0]

    if action == "Add Stop":
        index = int(data[1])
        string = data[2]
        if 0 <= index <= len(tour_stops):
            first_part = tour_stops[:index]
            second_part = tour_stops[index:]
            tour_stops = first_part + string + second_part
            print(tour_stops)

    elif action == "Remove Stop":
        index1 = int(data[1])
        index2 = int(data[2])
        if 0 <= index1 <= index2 < len(tour_stops):
            first_part = tour_stops[:index1]
            second_part = tour_stops[index2 + 1:]
            tour_stops = first_part + second_part
        print(tour_stops)

    elif action == "Switch":
        city = data[1]
        new_city = data[2]
        tour_stops = tour_stops.replace(city, new_city)
        print(tour_stops)

    command = input()

print(f"Ready for world tour! Planned stops: {tour_stops}")