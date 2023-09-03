n,m = map(int, input().split());
ans = True;
for i in range(n+1, m):
    if (2**i)%i==2:
        ans = False;
print(['NO','YES'][ans]);