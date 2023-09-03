n, a = map(int, input().split())
i = 1
c = 0
if a%2 != 0:
    while i != a:
        c = c + 1
        i += 2
    print(c+1)
i = n
if a%2 == 0:
    while i != a:
        c += 1
        i -= 2
    print(c+1)