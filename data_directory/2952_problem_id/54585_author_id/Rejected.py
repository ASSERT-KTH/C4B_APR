n,k=list(map(int,input().split(" ")))
if ((n%k)%2==0 or (n%k)%2==1) and n!=k:
 print("NO")
else:
 print("YES")