provisions = input().split(" ") #така се прави лист от който после да стане речника- BREAD 10 MILK 15 WATER 20
bakery = {}

for item in range(0, len(provisions), 2):
                                            #така се върти по цикъла по ИНДЕКСИ със стъпка 2, за да се вкара в речника {'продукт': количество}
    food = provisions[item]
    quantity = int(provisions[item + 1])    # тук в случая ни трябва число, затова е инт

    bakery[food] = quantity         #ТАКА СТАВА СДВОЯВАНЕТО В РЕ1НИКА Т.Е
                                    # {'BREAD': 10, 'MILK': 15}||||| виж че тук се ползва вече речника(bakery), а не листа!!!

                                    # при речниците няма нужда от append-е така се пълнят
print(bakery)