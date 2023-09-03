n=int(input())
s=input()
if s.count('7')+s.count('4')!=len(s):
    print("NO")
else:
    s1=0
    s2=0
    for i in s[:n//2]:
        s1+=int(i)
    for i in s[n//2:]:
        s2+=int(i)
    if s1==s2:
        print("YES")
    else:
        print("NO")