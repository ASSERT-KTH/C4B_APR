s = input()
c = 0
i = 1
t=s[0]
while c != 7 and i < len(s):
    if s[i] == t:
        c += 1
    else:
        t = s[i]
        c = 0
    i += 1
if c == 7:
    print("YES")
else:
    print("NO")