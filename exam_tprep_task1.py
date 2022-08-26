from math import ceil
command = input()
computer_price = 0

while command != "special" and command != "regular":
    parts_price = float(command)

    if parts_price >= 0:
        computer_price += parts_price
    else:
        print('Invalid price!')

    total_price_no_disc = computer_price + (computer_price * 0.2)
    command = input()

    if computer_price == 0:
        print("Invalid order!")

    final_price = computer_price * 1.2

    if command == "special":
        print("Congratulations, you've bought new computer!")
        print(f"Price without taxes {computer_price}")
        print(f'Taxes {computer_price * 0.2:.2f}')
        print("-----------")
        print(f"Total price: {final_price * 0.9}")
        break
    elif command == 'regular':
        print("Congratulations, you've bought new computer!")
        print(f"Price without taxes {computer_price}")
        print(f'Taxes {computer_price * 0.2:.2f}')
        print("-----------")
        final_price = round(final_price * 0.9)
        print(f"Total price: {final_price:.2f}")
        break
