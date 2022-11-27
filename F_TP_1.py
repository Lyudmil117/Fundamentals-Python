text = input().split("\\")
new = []
for string in text:
    if "." in string:
        new.append(string)


to_print = ("".join(new).split("."))

print(f'File name: {to_print[0]}')
print(f'File extension: {to_print[1]}')