import re
s=input()
s=input()
l=0
a=0
for i in range(len(s)):
    if i==0 or s[i-1]!=s[i]:
        a+=l
        l=0
    else:
        l+=1
print(a+l)