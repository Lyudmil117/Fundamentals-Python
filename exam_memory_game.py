sequence_of_elements = input().split()
command = input()
counter = 0
hit_all_matching_elements = False
found_element = ''
while not command == 'end':
    first_index_selected = int(command.split()[0])
    second_index_selected = int(command.split()[1])
    if first_index_selected != second_index_selected:
        if first_index_selected in range(len(sequence_of_elements)) \
                and second_index_selected in range(len(sequence_of_elements)):
            counter += 1
            if sequence_of_elements[first_index_selected] == sequence_of_elements[second_index_selected]:
                print(f'Congrats! You have found matching elements - {sequence_of_elements[first_index_selected]}!')
                found_element = sequence_of_elements[first_index_selected]
                sequence_of_elements.remove(found_element)
                sequence_of_elements.remove(found_element)
                if len(sequence_of_elements) == 0:
                    hit_all_matching_elements = True
            else:
                print('Try again!')
        elif first_index_selected < len(sequence_of_elements) \
                or second_index_selected < len(sequence_of_elements):
            if not hit_all_matching_elements:
                counter += 1
                left_half = len(sequence_of_elements) // 2
                sequence_of_elements.insert(left_half, f'-{counter}a')
                sequence_of_elements.insert(left_half, f'-{counter}a')
                print('Invalid input! Adding additional elements to the board')

    elif first_index_selected == second_index_selected:

        if not hit_all_matching_elements:
            counter += 1
            left_half = len(sequence_of_elements) // 2
            sequence_of_elements.insert(left_half, f'-{counter}a')
            sequence_of_elements.insert(left_half, f'-{counter}a')
            print('Invalid input! Adding additional elements to the board')

    command = input()

if len(sequence_of_elements) > 0:
    print('Sorry you lose :(')
    print(' '.join(sequence_of_elements))
else:
    print(f'You have won in {counter} turns!')

    
