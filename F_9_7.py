employ_happiness = list(map(int, input().split(" ")))
new_list = []
factor = int(input())
happy_people = []
for empl in employ_happiness:
    man = empl * factor
    new_list.append(man)

average = sum(new_list) / len(new_list) # 6.5
for person in new_list:
    if person >= average:
        happy_people.append(person)

if len(happy_people) >= len(new_list) / 2:
    print(f"Score: {len(happy_people)}/{len(new_list)}. Employees are happy!")
else:
    print(f'Score: {len(happy_people)}/{len(new_list)}. Employees are not happy!')
