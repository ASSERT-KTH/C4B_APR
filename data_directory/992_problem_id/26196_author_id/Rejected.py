n,m,z = map(int,input().split(' '))
i = n*m
if n > z or m == 0:
    ans = 0
else:
    ans = 1
    while i < z and abs(z-i) >= n*m:
        i += n*m
        ans += 1     
print(ans)