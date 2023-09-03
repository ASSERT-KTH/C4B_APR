s = str(input())

i = 0
zero = 0
zeroS = 0
one = 0
oneS = 0

while (i < len(s)):
    if (s[i] == '0'):
        one = 0
        zero += 1
        if (zeroS < zero):
            zeroS =  zero
    else:
        zero = 0
        one += 1
        if (oneS < one):
            oneS = one
    i +=1

if ((oneS >= 7)or(zeroS >= 7)):
    print("YES")
else:
    print("NO")