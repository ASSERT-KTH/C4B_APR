s=input()
k,n,z=0,len(s)//2,len(s)
for i in range(n):
    if s[i]!=s[z-i-1]:k+=1
if k!=1:
    print("NO")
else:
    print("YES")