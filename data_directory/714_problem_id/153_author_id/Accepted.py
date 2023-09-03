#n = int(input())
n, m, l, r, k = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
x = max(n, l)
y = min(m, r)
l = y - x + 1
if x <= k and k <= y:
    l -= 1
print(max(0, l))