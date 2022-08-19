todo = ["" for i in range(11)]

command = input()

while command != "End":
    the_input = command.split("-")

    priority = the_input[0]
    pri_num = int(priority)
    task = the_input[1]
    todo[pri_num] = task
    command = input()

final_list = [task for task in todo if task != ""]

print(final_list)
