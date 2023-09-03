s = input()
for i in range(1,len(s)):
    if ord(s[i]) > 90:
        print(s)
        exit()
if ord(s[0]) > 90:
    print(s[0].upper() + s[1:].lower())
else:
    print(s.lower())