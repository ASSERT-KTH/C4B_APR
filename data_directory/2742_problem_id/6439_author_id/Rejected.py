n = int(input())
if((n & 1) == 0):
    print('1' * (n >> 1))
else:
    n -= 3
    print('7', '1' * (n >> 1))