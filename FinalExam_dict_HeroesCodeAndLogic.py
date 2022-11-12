count = int(input())
heroes = {}

for _ in range(count):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hero_HP = int(current_hero[1])
    hero_MP = int(current_hero[2])

    heroes[hero_name][hero_HP] = hero_MP   # така става {ime: {hp: число , mp: число}}
    heroes[hero_name][hero_MP] = hero_MP

    # # а може и така:
    # да направя отделен речник и да го вкарам после в големия речник (heroes)
    # current_hero_dict = {}
    # current_hero_dict[hero_name][hero_HP] = hero_HP
    # current_hero_dict[hero_name][hero_MP] = hero_MP
    # heroes[hero_name] = current_hero_dict # eto tuk go vkarvam

command = input()

while command != "End":
    command_params = command.split(" - ")

    command_name = command_params[0]
    hero_name = command_params[1]
    value = int(command_params[2])

    if command_name == "Heal":
        if heroes[hero_name]['HP'] + value > 100:      #така достъпвам HP във вложения речник

            value = 100 - heroes[hero_name]['HP']      # така ще взема value за да мога да го разпечатам
            heroes[hero_name]['HP'] = 100               # не могат да са повече от 100, затова го правя 100 ако са повече
            print(f"{hero_name} healed for {value} HP!")

        else:
            heroes[hero_name]['MP'] += value
            print(f"{hero_name} healed for {value} HP!")

    elif command_name == "Recharge":
        if heroes[hero_name]['MP'] + value > 200:

            value = 200 - heroes[hero_name]['MP']
            heroes[hero_name]['MP'] = 200
            print(f"{hero_name} recharged for {value} MP!")

        else:
            heroes[hero_name]['MP'] += value
            print(f"{hero_name} recharged for {value} MP!")


    elif command_name == "TakeDamage":
        attacker = command_params[3]     #  в този случай има и атакуващ в command_name[3]

        heroes[hero_name]['HP'] -= value

        if heroes[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {value} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            heroes.pop(hero_name)     #ако е умрял го махни с heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")


    elif command_name == "CastSpell":
        spell_name = command_params[3]   # тук пак имам нещо ново в command_params и так си го взимам
        if heroes[hero_name]["HP"] >= value:
            heroes[hero_name]["HP"] -= value
            print(f"{hero_name} has successfully cast{spell_name} and now has {heroes[hero_name]['MP']} MP")

        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}')

    command = input()


for hero in heroes:
    print(f'{hero}')
    print(f"  HP {heroes[hero]['HP']}")  #hero а не heros_name , защото въртя ТУК в речника HEROES s "hero", a ne s hero_name
    print(f"  MP {heroes[hero]['MP']}")
