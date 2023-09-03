s = input()
for i in range(1,len(s)):
    if ord(s[i]) > 90:
        print(s)
        exit()
print(s[0].upper() + s[1:].lower())