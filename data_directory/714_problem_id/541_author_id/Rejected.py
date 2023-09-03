# Description of the problem can be found at http://codeforces.com/problemset/problem/714/A

l1, r1, l2, r2, k = map(int, input().split())
t = max(min(r1, r2) - max(l1, l2), 0) + 1

if (k >= l2 and k <= r2) and (k >= l1 and k <= r1):
    t -= 1

print(t)