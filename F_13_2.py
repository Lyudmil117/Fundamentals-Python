import re

string = input()
pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'  #виж знака "|" който тук се използава да го направиш:
                                                          # или с тире да са номерата или празно място
matches = re.findall(pattern, string)

print(", ".join(matches))