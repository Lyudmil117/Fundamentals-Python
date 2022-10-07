def even():
    filtered = filter(lambda num: num % 2 == 0, list1) # here you you put function(condition), then the sequence(list in that case)
    print(list(filtered))             #here you print it as a list


list1 = input().split(' ')
list1 = list(map(int, list1))

even()

