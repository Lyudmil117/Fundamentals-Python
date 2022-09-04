
words = input().split(' ')
output = ""

for char in words:
    output += char * len(char) #here add CHAR multiplied by its leght


print(output)
