products = input().split(" ")
bakery = {}

for item in range(0, len(products), 2):
    food = products[item]
    quantity = int(products[item + 1])

    bakery[food] = quantity # при речниците няма нужда от append-е така се пълнят

searched_products = input().split(" ") #новия лист

for searched in searched_products: #да проверя дали има това дето го търся от serched_products В bakery
    if searched in bakery:     #a тоя подукт от цикъла има ли го в речника?
        print(f"We have {bakery[searched]} of {searched} left")
    else:
        print(f"Sorry, we don't have {searched}")

