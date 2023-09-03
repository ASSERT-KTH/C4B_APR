n = int(input())
m = 0
p = 2
if n == 1:
    print(1)
elif n == 2:
    print(3)
elif n > 2:
    for i in range(n - 2 , 0, -1):
        m += i * p + 1
        p += 1
    print(n + m + 1)