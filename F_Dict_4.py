text = input()
courses = {}

while ":" in text:
    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses.keys():  #може и без keys/ тук проверчвам дали го има в курсовете
                                      #ако го няма го създавам
        courses[course] = {}          # така създавам ГОЛЕМИЯ КУРС, а другите ще бъдат вложени

    courses[course][id] = name      # РЕЧНИК = { КУРС : {ID (КЛЮЧ) : ИМЕ}} NESTED DICTIONARY

    text = input()


text = text.replace("_", " ")     #така на като получа WORD_SOMETHING , ЩЕ СТАНЕ WORD SOMETHING
                                  # СТАВА И С: COURSE = " ".JOIN(TEXT.SPLIT("_") ---така ще заменя подчертавката с празно място

for id in courses[text]:
    print(f'{courses[text][id]} - {id}')

    
