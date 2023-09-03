s = input()
a = s.split()
n = int(a[0])
b = int(a[1])
p = int(a[2])
t = n
c = 1
sm = 0
while True:
    while True:
        if c * 2 > n:
            break
        c *= 2
    sm = sm + c//2 + c*b
    n -= c//2
    if n == 1:
        break
    c = 1
print(sm, t * p, end = " ")