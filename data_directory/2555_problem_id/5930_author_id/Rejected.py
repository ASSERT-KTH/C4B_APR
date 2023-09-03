n=input()
k=len(n)
m=0
j=0
for i in range(k-1):
    if(n[i]==n[i+1]):
        j=j+1
    if(n[i]!=n[j]):
        j=0
    if(j>m):
        m=j
if(m>=6):
    print("YES")
else:
    print("NO")