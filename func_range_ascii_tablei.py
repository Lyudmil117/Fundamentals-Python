def char_in_range(ch1, ch2):
    for i in range(ord(ch1) + 1, ord(ch2)):  # +1 because we want to preint from next ascii item, not from this one
                                             #this is how you get something from ascii table ord(number of ascii item)
        print(chr(i), end=' ')               #by chr(i) we take currnet number and comvert it to correspondig item from ascii table


char1 = input()
char2 = input()
char_in_range(char1, char2)             # ВАЖНО!!! ТУК МОЖЕ ДА Е CHAR1/CHAR2, А ГОРЕ МОЖЕ ДА Е CH1/CH2 (ТОВА Е ОК)

