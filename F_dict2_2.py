dict = {}  # gold 134 silver 34 copper 56

while True:
    ore = input()
    if ore == "stop":
        break

    quantity = int(input())

    if ore not in dict:
        dict[ore] = quantity # ако ore го няма в речника го създай
    else:
        dict[ore] += quantity # ако го има го прибави

for key, value in dict.items():
    print(f'{key} -> {value}')
