password = input()
command = input()

while command != "Done":
    data = command.split(" ")
    action = data[0]

    if action == "TakeOdd":
        odd_password = ""
        for char in range(len(password)):
            if char % 2 != 0:
                odd_password += password[char]  # така взимам буквите от password чрез индексация
        password = odd_password
        print(password)

    elif action == "Cut":
        index = int(data[1])
        length = int(data[2])

        word = password[index:index + length]  #така намирам коя е думата дето трябва да се изреже от Password
        password = password.replace(word, "", 1)

        print(password)

    elif action == "Substitute":
        substring = data[1]
        substitute = data[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")