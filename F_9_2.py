train = [0] * int(input())
command = input().split(" ")
people_in_last_wagon = 0
current_wagon = 0
people_to_add = 0
people_to_leave = 0
new = 0
#train = [0] * number  #this is how you can create list of zeroes

while command[0] != "End":

    if command[0] == "add":
        last_wagon = train[-1]
        people = int(command[1])

        people_in_last_wagon += people
        train[-1] = people_in_last_wagon

    elif command[0] == "insert":
        index = int(command[1])
        people_to_add = int(command[2])
        train[index] += people_to_add

    elif command[0] == "leave":
        index_wagon = int(command[1])
        current_wagon = train[index_wagon]
        people_to_leave = int(command[2])

        train[index_wagon] = current_wagon - people_to_leave

    command = input().split(" ")

print(train)
