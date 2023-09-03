n = int(input())
s = n
while n%2==0:
    n //= 2
    s += n
print(s)