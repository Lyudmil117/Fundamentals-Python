def char_in_range():
    a = ord(input())
    b = ord(input())
    for character in range(a + 1, b):
        print(chr(character), end=" ")


char_in_range()