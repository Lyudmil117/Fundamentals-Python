text = input()
final_text = ""
command = input()

while command != "Reveal":
    data = command.split(":|:")
    action = data[0]

    if action == "InsertSpace":
        index = int(data[1])
        first_part = text[:index]
        second_part = text[index:]
        text = first_part + " " + second_part
        print(text)

    elif action == "Reverse":
        substring = data[1]
        if substring in text:
            new = substring[::-1]
            text = text.replace(substring, '', 1) # 1 защото така искаме да махнем само ПЪРВОТО СЪВПАДЕНИЕ
            text = text + new
            print(text)
        else:
            print("error")

    elif action == "ChangeAll":
        string1 = data[1]
        string2 = data[2]
        text = text.replace(string1, string2)
        print(text)

    command = input()

print(f'You have a new text message: {text}')