list_targets = list(map(int, input().split(" ")))
counter = 0
command = input()

while command != "End":
    index = int(command)

    if index > len(list_targets) - 1:
        pass

    else:
        current_target = list_targets[index]
        list_targets[index] = -1
        counter += 1

        for item in range(len(list_targets)):
            if list_targets[item] != -1 and list_targets[item] > current_target:
                list_targets[item] -= current_target
            elif list_targets[item] != -1 and list_targets[item] <= current_target:
                list_targets[item] += current_target

    command = input()

list_targets = list(map(str, list_targets))
list_targets = " ".join(list_targets)
print(f"Shot targets {counter} -> {list_targets}")
