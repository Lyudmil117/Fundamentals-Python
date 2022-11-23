import re

text = input()
list_pars = []
clean_list = []
pattern = r'#([A-Za-z]{3,})##([A-Za-z]{3,})#|@([A-Za-z]{3,})@@([A-Za-z]{3,})@'
matches = re.findall(pattern, text)
number_mirror_words = 0
pairs = 0
final_list = []
for_print = []
for match in matches:
    pairs += 1
    list_pars.append(match)

for tuple1 in list_pars:
    for item in tuple1:
        if len(item) > 0:
            clean_list.append(item)

for word in range(0, len(clean_list), 2):
    to_reverse = clean_list[word + 1]
    reversed_word = to_reverse[::-1]

    for first_word in range(len(clean_list)):
        if clean_list[word] == reversed_word:
            if clean_list[word] not in final_list:
                final_list.append(clean_list[word])


if pairs > 0:
    print(f'{pairs} word pairs found!')

    if len(final_list) > 0:
        print("The mirror words are:")
        for fuck in final_list:
            for_print.append(f'{fuck} <=> {fuck[::-1]}')
        print(", ".join(for_print))

    else:
        print("No mirror words!")

else:
    print("No word pairs found!")
    print("No mirror words!")





