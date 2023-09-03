n = int(input())
for i in range(n // 3):
    print('abc', end = "" )
if n % 3 == 1:
    print('a')
elif n % 3 == 2:
    print('ab')