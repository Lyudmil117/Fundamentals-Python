first_word, second_word = input().split(" ")
total_sum = 0

if len(first_word) > len(second_word):
    for index in range(len(second_word)):
        total_sum += ord(second_word[index]) * ord(first_word[index])
    for index in range(len(second_word), len(first_word)):
        total_sum += ord(first_word[index])
elif len(second_word) > len(first_word):
    for index in range(len(first_word)):
        total_sum += ord(first_word[index]) * ord(second_word[index])
    for index in range(len(first_word), len(second_word)):
        total_sum += ord(second_word[index])
else:
    for index in range(len(first_word)):
        total_sum += ord(first_word[index]) * ord(second_word[index])

print(total_sum)