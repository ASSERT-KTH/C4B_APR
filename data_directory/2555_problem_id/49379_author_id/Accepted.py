s = input()
zeros = '0000000'
ones = '1111111'
if (zeros in s) | (ones in s):
    print('YES')
else:
    print('NO')