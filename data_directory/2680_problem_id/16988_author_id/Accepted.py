a=[int(x) for x in input().split()]
n=a[0]
a=a[1:]
while len(a) < 10**6.5:
    a += [8787]
a.sort()
for i in range(n):
    print(a[i],end=' ' if i != n-1 else '\n')