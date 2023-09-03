n = int(input())
s = list()
k = -1
f = False
while n > 0:
    if -k > len(s) and n%4 != 0 and f:
        print(-1)
        break
    if n >= 7 and not f:
        n -= 7
        s += ['7']
    elif n % 4 == 0:
        t = n//4
        s += ['4'] * t
        n = 0
    else:
        s[k] = '4'
        n += 3
        k -= 1
        f = True
else:
    for i in reversed(s):
        print(i, end='')