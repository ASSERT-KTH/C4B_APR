k, a, b = [int(i) for i in input().split()]

res = a // k + b // k
if res == 0:
    print(-1)
else:
    print(res)