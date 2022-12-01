import re
num = int(input())
pattern = r'(\@[#?]+)([A-Z][a-zA-Z-0-9]{4,}[A-Z])(@(\#?)+)'


for _ in range(num):
    product_group = ''
    text = input()
    match = re.findall(pattern, text)
    if match:
        word = match[0][1]    # така достъпвам 0-група, 2-рото нещо в нея-ДУМАТА
        for i in word:
            if i.isdigit():
                product_group += i
        if len(product_group) == 0:
            print("Product group: 00")
        else:
            print(f'Product group: {product_group}')

    else:
        print("Invalid barcode")

# ОЩЕ ЕДИН НАЧИН

import re
n = int(input())
pattern = r'@#{1,}([A-Z][a-zA-Z0-9]{4,}[A-Z])@#{1,}'

for _ in range(n):
    text = input()
    list1 = []
    result = re.findall(pattern, text)
    for item in result:
        list1.append(item)
    if len(list1) == 0:
        print("Invalid barcode")
    else:
        numbers = ""
        for char in list1:
            word = "".join(list1)
            for i in word:

                if i.isdigit():
                    numbers += i
            if len(numbers) == 0:
                print("Product group: 00")
            else:
                print(f'Product group: {numbers}')

