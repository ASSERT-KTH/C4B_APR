n, t = map(int, input().split())
pp = input().strip()
ll = []
for j in pp:
    ll.append(j)
for i in range(t):
    k = 0
    while k < n-1:
        if ll[k] == 'B' and ll[k+1] == 'G':
            ll[k] = 'G'
            ll[k+1] = 'B'
            k += 1
        k += 1
print(''.join(ll))