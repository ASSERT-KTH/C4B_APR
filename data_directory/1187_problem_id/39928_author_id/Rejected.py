i = input()

if i[0] == i[0].lower() and i[1:] == i[1:].upper():
    print(i[0].upper() + i[1:].lower())
elif i.upper() == i:
    print(i[0].upper() + i[1:].lower())
else:
    print(i)