n = int(input())
l = list(map(int, input().split()))
s = sum(l)
if n > s:
    n = n % s
c = 0
for i in range(7):
    c += l[i]
    if c >= n:
        print(i + 1)
        exit()