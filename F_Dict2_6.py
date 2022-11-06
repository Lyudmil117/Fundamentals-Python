products_shop = {}
command = input()

while command != "buy":
    command = list(command.split(" "))
    product = command[0]  #key
    price = float(command[1])
    quantity = int(command[2])

    if product not in products_shop:
        products_shop[product] = []
        products_shop[product].append(price)
        products_shop[product].append(quantity)
    else:
        products_shop[product][0] = price
        products_shop[product][1] += quantity

    command = input()

for key, values in products_shop.items():
    print(f'{key} -> {(products_shop[key][0] * products_shop[key][1]):.2f}')
