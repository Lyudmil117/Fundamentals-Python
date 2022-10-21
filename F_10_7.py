sequence_of_numbers = [int(num) for num in input().split(', ')]
nums_counter = 0
group_list = 10
while len(sequence_of_numbers) > nums_counter:
    current_group = []
    for number in sequence_of_numbers:

        if group_list - 10 < number <= group_list:
            current_group.append(number)
            nums_counter += 1

    print(f"Group of {group_list}'s: {current_group}")
    group_list += 10
