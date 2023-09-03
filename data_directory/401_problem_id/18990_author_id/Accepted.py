a = int(input())
if a < 13:
    print(2**a)
else:
    start = 8092
    for _ in range(a - 13):
        start *= 2
    print(start)