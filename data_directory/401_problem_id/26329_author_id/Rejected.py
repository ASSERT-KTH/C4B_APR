n = int(input())
m = list(map(int, input().split()))
r = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if (i + 1) % m[i] == r[i]:
        cnt += 1
print(cnt / n)