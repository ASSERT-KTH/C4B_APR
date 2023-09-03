from sys import stdin
a, b, n = [int(x) for x in stdin.readline().rstrip().split()]
temp = a
for i in range(n):
    for x in range(10):
        if (a*10+x) % b == 0:
            a = a * 10 + x
            break
if temp == a:
    a = -1
print(a)