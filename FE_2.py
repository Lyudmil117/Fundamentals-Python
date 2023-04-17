import re
n = int(input())

pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

for _ in range(n):
    text = input()
    result = re.findall(pattern, text)
    if len(result) == 0:
        print("The message is invalid")
    else:
        lst = []
        for char in result[0][1]:
            lst.append(ord(char))
        clean = ""
        for i in lst:
            clean += " " + str(i)
        print(f'{result[0][0]}:{clean}')
        
