#n = int(input())
#n, m = map(int, input().split())
s = input()
#c = list(map(int, input().split()))
n = len(s)
l = 0
for i in range(n):
    if s[i] != s[n - 1 - i]:
        l += 1
if l != 2:
    print('NO')
else:
    print('YES')