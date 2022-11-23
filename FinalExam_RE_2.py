import re

text = input()
pattern = r'([=/])([A-Z][A-Za-z]{2,})\1'

matches = re.finditer(pattern, text)
points = 0
locations = []

for match in matches:
    city = match[2]
    locations.append(city)
    points += len(match[2])

print(f'Destinations: {", ".join(locations)}')
print(f"Travel Points: {points}")