n, l, r = map(int, input().split())

binl = tuple(map(int, bin(n)[2:]))

res = 0

for i in range(len(binl)):
    if not binl[i]:
        continue
    cur = 1 << i
    dif = 1 << (i + 1)
    while cur <= r:
        if cur >= l:
            res += 1
        cur += dif

print(res)