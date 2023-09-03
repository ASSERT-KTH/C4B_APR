s = input()
if s[1:].isupper():
    for c in s:
        if c.islower(): print(c.upper(), end='')
        else: print(c.lower(), end='')
else:
    print(s)