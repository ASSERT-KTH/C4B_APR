import sys

n = int(input())
an = list(map(int, sys.stdin.readline().split()))

total = sum(an)
n = n % total

ans = 0
while n > 0 and ans < 7:
    n -= an[ans]
    if n > 0:
        ans += 1
print(1 + ans)