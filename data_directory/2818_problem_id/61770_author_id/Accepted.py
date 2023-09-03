n = int(input())
for i in range(n // 4):
    print('aabb', end = "" )
if n % 4 == 1:
    print('a')
elif n % 4 == 2:
    print('aa')
elif n % 4 == 3:
    print('aab')