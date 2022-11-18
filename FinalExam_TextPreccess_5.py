activation_key = input()
command = input()

while command != "Generate":
    data = command.split(">>>")
    action = data[0]

    if action == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        to_delete = activation_key[start_index:end_index]         # така намирам кво да трия
        activation_key = activation_key.replace(to_delete, "")    #taka go maham ot Activation_key
        print(activation_key)

    elif action == "Flip":
        if data[1] == "Upper":
            start_index = int(data[2])
            end_index = int(data[3])
            to_change = activation_key[start_index:end_index]
            activation_key = activation_key.replace(to_change, to_change.upper())
            print(activation_key)

        elif data[1] == "Lower":
            start_index = int(data[2])
            end_index = int(data[3])
            to_change = activation_key[start_index:end_index]
            activation_key = activation_key.replace(to_change, to_change.lower())
            print(activation_key)

    elif action == "Contains":
        substring = data[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    command = input()

print(f"Your activation key is: {activation_key}")