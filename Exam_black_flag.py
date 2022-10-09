days_to_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0
target_plunder = False

for day in range(1, days_to_plunder + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += daily_plunder * 0.5
    if day % 5 == 0:
        total_plunder = total_plunder * 0.7


if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percent = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percent:.2f}% of the plunder.")
