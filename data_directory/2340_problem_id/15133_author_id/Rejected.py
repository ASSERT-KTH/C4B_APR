s = input()
i = 0
j = 0
for char in s:
    if ord(char) >= 97 and ord(char) <= 122:
        i += 1
    else:
        j += 1

if i == j:
    print(s.lower())
else:
    print(s.upper())