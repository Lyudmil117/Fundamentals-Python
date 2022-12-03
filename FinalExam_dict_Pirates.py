command = input()
cities = {}
while command != "Sail":
    data = command.split("||")
    city = data[0]
    population = int(data[1])
    gold = int(data[2])
    if city in cities:
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    else:
        cities[city] = {'population': population, 'gold': gold}
    command = input()

command = input()
while command != 'End':
    data = command.split("=>")
    action = data[0]
    if action == "Plunder":
        town = data[1]
        population_to_kill = int(data[2])
        gold_to_steal = int(data[3])
        cities[town]['population'] -= population_to_kill
        cities[town]['gold'] -= gold_to_steal

        print(f"{town} plundered! {gold_to_steal} gold stolen, {population_to_kill} citizens killed.")

        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            print(f'{town} has been wiped off the map!')
            cities.pop(town)

    elif action == "Prosper":
        town = data[1]
        gold_to_add = int(data[2])
        if gold_to_add < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]['gold'] += gold_to_add
            print(f"{gold_to_add} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    command = input()

if len(cities) > 0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for town in cities:
        print(f"{town} -> Population: {cities[town]['population']} citizens, Gold: {cities[town]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
