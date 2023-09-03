n = int(input())
m = n
a = list(map(int, input().split()))
s = sum(a)
n = n % s if n > s else n
r = 0
for i in range(7):
    if n > a[i]:
        n -= a[i]
    else:
        r = i
        break

print(r+1)