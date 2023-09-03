#n = int(input())
n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
l = m + n - 3
if (m - n) % 3 != 0:
    l += 1
print(max(l, 0))