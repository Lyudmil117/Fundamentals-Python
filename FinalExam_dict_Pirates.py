cities_to_attack = {}

command = input()
while command != "Sail":
    data = command.split("||")

    city = data[0]
    population = int(data[1])
    gold = int(data[2])

    if city in cities_to_attack:
        cities_to_attack[city][1] += gold
        cities_to_attack[city][0] += population
    else:
        cities_to_attack[city] = city
        cities_to_attack[city] = [population, gold]

    command = input()

command = input()

while command != "End":
    data2 = command.split("=>")
    action = data2[0]
    city = data2[1]

    if action == "Plunder":
        people_killed = int(data2[2])
        gold_to_plunder = int(data2[3])

        if cities_to_attack[city][0] <= 0 or cities_to_attack[city][1] <= 0:
            cities_to_attack.pop(city)
            print(f"{city} has been wiped off the map!")

        else:
            cities_to_attack[city][0] -= people_killed
            cities_to_attack[city][1] -= gold_to_plunder

            if cities_to_attack[city][0] > 0 and cities_to_attack[city][1] > 0:
                print(f"{city} plundered! {gold_to_plunder} gold stolen, {people_killed} citizens killed.")
            else:

                print(f"{city} plundered! {gold_to_plunder} gold stolen, {people_killed} citizens killed.")
                print(f"{city} has been wiped off the map!")
                cities_to_attack.pop(city)

    elif action == "Prosper":
        gold_to_add = int(data2[2])

        if gold_to_add < 0:
            print('Gold added cannot be a negative number!')
            pass
        else:
            cities_to_attack[city][1] += gold_to_add
            print(f'{gold_to_add} gold added to the city treasury. {city} now has {cities_to_attack[city][1]} gold.')

    command = input()

print(f"Ahoy, Captain! There are {len(cities_to_attack)} wealthy settlements to go to:")
for town in cities_to_attack:
    print(f'{town} -> Population: {cities_to_attack[town][0]} citizens, Gold: {cities_to_attack[town][1]} kg')
