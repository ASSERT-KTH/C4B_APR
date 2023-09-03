x = input()
x = str.split(x, ' ')
n = int(x[0])
m = int(x[1])

if n % m is 0:
    print(n + m)
else:
    p = n // m
    while True:
        temp = p * m
        if temp > n:
            print(temp)
            break
        p += 1