inputs = tuple(map(lambda x: int(x), input().split()))
n = inputs[0]
m = inputs[1]

if n == 0:
    print(m)
else:
    summery = (1 + n) * n / 2
    last = m % summery

    i = 1
    while last >= 0:
        last -= i
        i += 1

    last = int(last + i -1)

    print(last)