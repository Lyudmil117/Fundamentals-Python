data = list(map(int, input().split(", ")))
#this is how by MAP function we turn the input text from string to list with integers(now strings)

positive_list = [str(x) for x in data if x >= 0] #X must be a string so later we can join it down
negative_list = [str(x) for x in data if x < 0]
even_list = [str(x) for x in data if x % 2 == 0]
odd_list = [str(x) for x in data if x % 2 != 0]

print(f"Positive: {', '.join(positive_list)}") #here!
print(f'Negative: {", ".join(negative_list)}')# here we remove the [] because its wanted in the task
print(f'Even: {", ".join(even_list)}')
print(f'Odd: {", ".join(odd_list)}')

#IMPORTANT: if you use "" with the f(str) like here, then use '' when typing ', '.join(list) or the opposite way
