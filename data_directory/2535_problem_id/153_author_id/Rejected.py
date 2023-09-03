#n = int(input())
n, m = map(int, input().split())
#s = input()
c = list(map(int, input().split()))
i = 1
while i <= n and i <= m:
    m -= i
    i += 1
print(m)