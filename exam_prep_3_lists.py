targets = input().split(', ')
targets = list(map(int, targets))

line = input()

while line != "End":
    command_list = line.split('')
    command = command_list[0]
    index = int(command_list[1])
    value = int(command_list[2])

    if command == "Shoot" and 0 <= index < len(targets):
        curr_target = targets[index]
        curr_target -= value
        if curr_target <= 0:
            targets.pop(index)
        else:
            targets[index] = curr_target

    elif command == "Add":
        if 0 <= index <= len(targets):
            targets.insert(index, value)
        else:
            print("Invalid Placement")

    elif command == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:] # за да не правим нещо с индекса в центъра,а тия след него
            #Very important!!! By : (chech above) lsit[:someting] means "from the start of the list till this index
            #and list[index:] means from this index till the end of the list

        else:
            print("Strike Missed!")

    line = input()

targets = list(map(str, targets))
targets = "|".join(targets)
print(targets)
