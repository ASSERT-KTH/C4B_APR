s = input()
if s.isupper() or (s[0].lower() and (s[1:].isupper()) if len(s) > 1 else True):
    print(s[0].upper() + s[1:].lower())
else:
    print(s);