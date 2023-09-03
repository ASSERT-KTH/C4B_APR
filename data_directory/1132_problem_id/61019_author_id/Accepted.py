x=int(input())
c=[4,7,47,74,444,447,477,777,744,774,777]
a=0
for k in range (len (c)):
    if (x%c[k]==0):
        a=1
        break
if a==1:
    print("YES")
else:
    print("NO")