initial_energy = int(input())
won_battles = 0
distance_enemy = 0
command = input()

while True:
    if command == "End of battle":
        print(f'Won battles: {won_battles}. Energy left: {initial_energy}')
        break
    else:
        distance_enemy = int(command)

        if initial_energy >= distance_enemy:
            initial_energy -= distance_enemy
            won_battles += 1

            if won_battles % 3 == 0:
                initial_energy += won_battles

        elif initial_energy < distance_enemy:
            print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
            break

    command = input()