text = input().split(' ')
word = [word for word in text if len(word) % 2 == 0]
print('\n'.join(word)) #this is how you print the elements form string(word) on a new line


