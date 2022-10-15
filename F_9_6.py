list1 = input().split(" ")
palindrome = input()
palindrome_list = []
for word in list1:
    if word == word[::-1]:
        palindrome_list.append(word)

count_palindrome = palindrome_list.count(palindrome)

print(palindrome_list)
print(f"Found palindrome {count_palindrome} times")
