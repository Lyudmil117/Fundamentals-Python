def office_managment(number_of_rooms):
    left_chairs = 0
    condition = True # if this is TRUE then we will print number of free chairs, otherwise not
    free_chairs = 0
    for room in range(1, number_of_rooms + 1):
        data = input().split(' ')
        chairs = data[0]
        visitors = int(data[1])

        diff = abs(len(chairs) - visitors)

        if len(chairs) < visitors:
            condition = False
            print(f'{diff} more chairs needed in room {room}')

        elif len(chairs) > visitors:
            free_chairs += diff

    if condition:                            #Here i fuck up-because i could not figure out if in some of the
        print(f'Game on,{free_chairs} left')  #room if trere are free chairs nothing must happen(no print)


num_rooms = int(input())
office_managment(num_rooms)
