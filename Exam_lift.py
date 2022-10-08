people_waiting = int(input())
current_lyft_empty_seats = input().split(" ")
total_seats = len(current_lyft_empty_seats) * 4
current_lyft_empty_seats = list(map(int, current_lyft_empty_seats))
seated = 0

people_waiting_left = people_waiting

for cabin in range(len(current_lyft_empty_seats)):
    while current_lyft_empty_seats[cabin] < 4 and people_waiting_left > 0:
        if people_waiting > 0:
            current_lyft_empty_seats[cabin] += 1
            people_waiting_left -= 1
            seated += 1

        if people_waiting == 0:
            break


current_lyft_empty_seats = list(map(str, current_lyft_empty_seats))

if (people_waiting - seated) > 0:
    print(f"There isn't enough space! {people_waiting_left} people in a queue!")
    print(" ".join(current_lyft_empty_seats))
else:
    print("The lift has empty spots!")
    print(" ".join(current_lyft_empty_seats))


