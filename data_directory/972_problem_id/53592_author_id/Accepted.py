R= lambda: map(int,input().split())
n,l= R()
if (n!=0 or l!=0) and (n-l==0 or n-l==-1 or n-l==1):    print("YES")
else:   print("NO")