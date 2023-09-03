import re

s = input()

upper = re.findall('[A-Z]', s)
lower = re.findall('[a-z]', s)

if len(upper) > len(lower):
    print(s.upper())
else:
    print(s.lower())