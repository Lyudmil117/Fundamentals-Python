list1 = list(map(int, input().split(" ")))
command = input().split(" ")
lst2 = []
while command[0] != "end":

    if command[0] == "swap":
        ind1 = int(command[1])
        ind2 = int(command[2])
        list1[ind1], list1[ind2] = list1[ind2], list1[ind1]
    elif command[0] == "multiply":
        ind1 = int(command[1])
        ind2 = int(command[2])

        num1 = int(list1[ind1])
        num2 = int(list1[ind2])

        list1[ind1] = num1 * num2

    elif command[0] == "decrease":
        for num in range(len(list1)):
            list1[num] -= 1     #this is how to decrease all elements in list by -1

    command = input().split(" ")

    
list1 = list(map(str, list1))
print(" ".join(list1))
