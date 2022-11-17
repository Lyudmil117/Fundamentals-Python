message = input()
command = input() # otvarqi si ochite malko!!!

while command != "Decode":

    data = command.split("|")
    action = data[0]

    if action == "ChangeAll":
        letter_one = data[1]
        letter_two = data[2]
        message = message.replace(letter_one, letter_two)

    elif action == "Insert":
        index = int(data[1])
        letter = data[2]
        first_part = message[:index]
        second_part = message[index:]
        message = first_part + letter + second_part

    elif action == "Move":
        index = int(data[1])
        first_part = message[:index]
        second_part = message[index:]
        message = second_part + first_part

    command = input()

print(f"The decrypted message is: {message}")