k, a, b = [int(i) for i in input().split()]

resa = a // k
resb = b // k
osta = a % k
ostb = b % k

res = resa + resb

if (res == 0) or (resa == 0 and ostb != 0) or (resb == 0 and osta != 0):
    print(-1)    
else:
    print(res)