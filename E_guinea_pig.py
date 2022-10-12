food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000
remain_food = 0


for day in range(1, 30 + 1):
    remain_food = food - 300
    if remain_food < (food - 300):
        break
    if day % 2 == 0:
        hay -= remain_food * 0.05
        if hay < (remain_food * 0.05):
            break

    if day % 3 == 0:
        cover -= pig_weight / 3
        if cover < (pig_weight / 3):
            break

    food = remain_food

    

if remain_food < 300 or hay < (remain_food * 0.95) or cover < (pig_weight / 3):
    print("Merry must go to the pet store!")

else:
    print(f"Everything is fine! Puppy is happy! Food: {(remain_food / 1000):.2f}, Hay: {(hay / 1000):.2f}, Cover: {(cover / 1000):.2f}.")
