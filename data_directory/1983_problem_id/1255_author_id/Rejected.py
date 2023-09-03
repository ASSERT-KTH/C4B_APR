n = int(input())
m = 0
p = 2
for i in range(n - 2 , 0, -1):
    m += i * p + 1
    print(i,p)
    p += 1
    print(n + m + 1)