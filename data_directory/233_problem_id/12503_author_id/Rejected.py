n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = b - c
if n < a and n < b:
    count = 0
else:
    if a <= d:
        count = n//a
    else:
        count, _ = divmod(n-c, d)
        count += (n-count*d)//a
print(count)