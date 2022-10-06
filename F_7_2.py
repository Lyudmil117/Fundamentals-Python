def grades():
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        print("Fail")
    elif grade <= 3.49:
        print("Poor")
    elif grade <= 4.49:
        print('Good')
    elif grade <= 5.49:
        print('Very Good')
    else:
        print("Excellent")

grades()
