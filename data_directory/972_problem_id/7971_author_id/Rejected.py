n,m = map(int , input().split())
if n==m:
       print("YES")
elif n+1==m or n-1==m:
       print("YES")
elif n==0 and m==0:
       print("NO")
else:
       print("NO")