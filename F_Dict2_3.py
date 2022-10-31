
county = input().split(", ")
capital = input().split(", ")
geography = {county: capital for county, capital in zip(county, capital)}
# list comprehension  taka sus ZIP moje da se sdvoqt COUNTRY: CAPITAL

for county, capital in geography.items():

    print(f'{county} -> {capital}')