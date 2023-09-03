k = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
d = 0
m = 0
for i in range(12):
    d += a[i]
    m += 1
    if d >= k:
        break
    
if k == 0:
    print('0')
elif d < k:
    print('-1')
else:
    print(m)