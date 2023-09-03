n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = b - c
count = 0
if a <= d or a <= n and b > n:
    count = n//a
elif n >= b:
    count, _ = divmod(n-c, d)
    count += (n-count*d)//a
print(count)