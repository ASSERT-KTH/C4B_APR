##n = int(input())
##a = list(map(int, input().split()))
##print(" ".join(map(str, res)))

n = int(input())

d = int(n/7)
r = n%7
vmin = 2*d
vmax = 2*d+min(2, r)
if r == 6:
    vmin = vmin+1
print(vmin, vmax)