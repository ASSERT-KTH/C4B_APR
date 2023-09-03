def dragons(l):
    n = l[4]
    l = sorted(l[:4])
    for i in range(3):
        for j in range(i + 1, 4):
            if l[i] != 0 and l[j] % l[i] == 0:
                l[j] = 0
    l = [x for x in l if x != 0]
    r = 0
    for i in range(n):
        for j in range(len(l)):
            if i % l[j] == 0:
                r += 1
                break
    return r

k = int(input().strip())
l = int(input().strip())
m = int(input().strip())
n = int(input().strip())
d = int(input().strip())
print(dragons([k, l, m, n, d]))