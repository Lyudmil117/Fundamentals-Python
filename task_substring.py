search_word = input()
text = input()

while search_word in text:
    text = text.replace(search_word, "") #replace serch word by empty string(like deleting it almost...)
    #note here that i have to store the upper result in variable "text", otherwise the loop will be endless!

print(text)
