n = int(input())
while n & 1 == 0:
    n >>= 1
print(n >> 1)