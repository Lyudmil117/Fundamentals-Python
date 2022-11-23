import re
num = int(input())
pattern = r'(\@[#?]+)([A-Z][a-zA-Z-0-9]{4,}[A-Z])(@(\#?)+)'


for _ in range(num):
    product_group = ''
    text = input()
    match = re.findall(pattern, text)
    if match:
        word = match[0][1]
        for i in word:
            if i.isdigit():
                product_group += i
        if len(product_group) == 0:
            print("Product group: 00")
        else:
            print(f'Product group: {product_group}')

    else:
        print("Invalid barcode")

