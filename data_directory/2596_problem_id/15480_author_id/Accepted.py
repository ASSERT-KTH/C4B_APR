n, l, r = map(int, input().split())

binl = tuple(map(int, bin(n)[2:]))

# print(binl)

res = 0

for i in range(len(binl)):
    if not binl[i]:
        # print(i, binl[i], "skipped")
        continue
    cur = (1 << i) + (((l >> (i + 1)) - 1) << (i + 1))
    # print(i, cur)
    dif = 1 << (i + 1)
    while cur <= r:
        if cur >= l:
            res += 1
        cur += dif

print(res)