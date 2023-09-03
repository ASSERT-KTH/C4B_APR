import sys
s = sys.stdin.read().strip().split("\n")
s = s[0]
c = 0
p = -1
for i in range(len(s)):
    if s[i]!=p:
        c=0
        p=s[i]
    else:
        c+=1
        if c==7:
            break
if c==7:
    print("YES")
else:
    print("NO")