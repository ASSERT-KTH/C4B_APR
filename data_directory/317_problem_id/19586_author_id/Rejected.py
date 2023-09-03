n, a = map(int, input().split())

def odd(a):
    c = 0
    i = 1
    while i <= n-2:
        i += 2
        c += 1
    return c

def even(a):
    c = 0
    i = n
    while i >= 2:
        i -= 2
        c += 1
    return c
if a % 2 == 0:
    print(even(a))
else:
    print(odd(a))