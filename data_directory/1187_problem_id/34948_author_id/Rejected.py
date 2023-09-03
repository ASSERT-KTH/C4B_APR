s=input()

if len(s)==1:
    s=s.capitalize()
else:
    if s[0].islower() and s[1:].isupper():
        s=s.swapcase()
    if s.isupper():
        s=s.swapcase()
print(s)