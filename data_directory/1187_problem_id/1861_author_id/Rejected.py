s = input()

if len(s) == 1:
    s = s.upper()
elif s.isupper():
    s = s.lower()
else:
    if s[0].islower() and s[1:].isupper():
        s = s[0].upper() + s[1:].lower()
print(s)