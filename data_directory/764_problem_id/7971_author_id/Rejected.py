n,m, k  = map(int , input().split())
f = (n+m+k)//3
print(abs(n-f) + abs(m-f) + abs(k-f))