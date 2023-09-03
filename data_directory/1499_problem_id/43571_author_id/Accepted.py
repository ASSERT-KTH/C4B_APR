n = int(input())
m = 1000000007
n = pow(2,n,m)
print((((n % m) * ((n + 1) % m)) // 2) % m)