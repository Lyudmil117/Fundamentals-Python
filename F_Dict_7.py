count = int(input())
dictionary = {}

for i in range(count):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = list()  # here we create KEY: and empty list [] 

    dictionary[word].append(synonym) #here we start to append synonyms to the empty the empty list


for word in dictionary:
    synonyms = ", ".join(dictionary[word])
    print(f'{word} - {synonyms}')
