y = int(input())
while y < 9000:
    y += 1
    s = str(y)
    if (s[0]!=s[1] and s[0]!=s[2] and s[0]!=s[3] and s[1]!=s[2] and s[1]!=s[3] and s[2]!=s[3]):
        print (s)
        break