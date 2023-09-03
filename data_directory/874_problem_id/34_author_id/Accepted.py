n, k  = map(int, input().split())


while k != 2 ** n:
    if k < 2 ** n:
        k  = k
    else:
        k -= 2**n
    n -= 1

print(n+1)