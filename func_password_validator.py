import re


def password(passw):
    val = False
    if len(passw) < 6 or len(passw) > 10:
        val = True
        print("Password must be between 6 and 10 characters")

    if not passw.isalnum():
        val = True
        print("Password must consist only of letters and digits")

    if passw.isalpha():
        val = True
        print(f'Password must contain at least two digits')

    if not val:
        print('Password is valid')


passw = input()
password(passw)
