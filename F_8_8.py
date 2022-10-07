numbers = input().split(", ")


def palindromes():
    for element in numbers:
        if element == element[::-1]:
            print("True")
        else:
            print("False")


palindromes()
