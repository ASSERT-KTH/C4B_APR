k = int(input())
m  = [int(i) for i in input().split()]
m.sort()
m = m[::-1]
months = 0
g = 0
if sum(m) < k:
    print(-1)
else:
    while g < k:
        g += m[months]
        months += 1
print(months)