#n = int(input())
n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
i = 1
while i <= m:
    m -= i
    i += 1
    if i > n:
        i = 1
print(m)