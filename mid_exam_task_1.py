num_of_cites_to_visit = int(input())
total_profit = 0

for cite in range(1, num_of_cites_to_visit + 1):
    city = input()
    earned = float(input())
    expenses = float(input())
    current_city_profit = 0

    if cite % 3 == 0 and cite % 5 != 0:
        expenses = expenses * 1.5
    if cite % 5 == 0:
        earned = earned * 0.9

    current_city_profit = earned - expenses
    total_profit += current_city_profit

    print(f'In {city} Burger Bus earned {current_city_profit:.2f} leva.')
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
