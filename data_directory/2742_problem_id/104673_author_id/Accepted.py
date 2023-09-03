n = int(input())
res = ''
while n >= 2:
    n -= 2
    res += '1'

if n == 1:
    res = '7' + res[:-1]
print(res)