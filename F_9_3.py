list1 = []

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split("-")
    priority = int(split_command[0])
    task = split_command[1]
    list1.append((priority, task)) #NEW SKILL виж как се прибавят и двете и ще стане [[ x y], [a b], [t t]]или вложени списъци


list2 = [task[1] for task in sorted(list1)]   #task[1] zastoto sa  (1 walk the dog) например, а на нас ни
                                                #ни трябва само второто
print(list2)

