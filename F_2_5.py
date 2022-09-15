

number_orders = int(input())
total_price = 0

for orders in range(number_orders):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    rules = [0.01 <= price_capsule <= 100, 1 <= days <= 31,  # this row
             1 <= capsules_per_day <= 2000]  # this row
    if not all(rules):  # this row
        continue  # this row
    current_price = (days * capsules_per_day) * price_capsule
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")
print(f"Total: ${total_price:.2f}")