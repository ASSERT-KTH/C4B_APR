c, v0, v1, a, l = map(int, input().split())

days = 1
i = 1
c -= v0
while c > 0:
    toread = v0 + i * a

    if toread > v1:
        toread = v1

    toread -= l
    c -= toread
    i += 1
    days += 1

print(days)