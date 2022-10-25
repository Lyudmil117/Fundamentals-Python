list_phones = input().split(", ")

while True:
    command = input()
    if command.lower() == "end":
        break

    action = command.split(" - ")
    if action[0] == "Add":
        if (action[1] not in list_phones):
            list_phones.append(action[1])

    if action[0] == "Remove":
        if (action[1] in list_phones):
            list_phones.remove(action[1])


    if action[0] == "Last":
        if (action[1] in list_phones):
            list_phones.remove(action[1])
            list_phones.append((action[1]))

    if action[0] == "Bonus phone":
        bonus_action = action[1].split(":")
        if (bonus_action[0] in list_phones):
            index = list_phones.index(bonus_action[0])
            list_phones.insert(index+1,bonus_action[1])


print(", ".join(list_phones))