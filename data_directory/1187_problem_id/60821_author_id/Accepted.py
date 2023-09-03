s = input()
if not s[1:] or s[1:].isupper():
    if (s[0].islower()):
        print(s[0].upper() + s[1:].lower())
    else:
        print(s[0].lower() + s[1:].lower())
else:
    print(s)