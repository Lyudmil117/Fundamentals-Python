number = int(input())


def bar():
    remain = 100 - number
    a = chr(37)
    b = chr(46)
    perc = int(number / 10)
    dots = int(remain / 10)
    if number == 100:
        print("100% Complete!")
        print(f'[{(perc * a)+(dots * b)}]')
    else:
        print(f"{number}% [{(perc * a)+(dots * b)}]")
        print("Still loading...")


bar()
