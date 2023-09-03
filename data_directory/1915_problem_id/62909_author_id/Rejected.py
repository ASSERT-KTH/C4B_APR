"""http://codeforces.com/problemset/problem/255/A"""

n = int(input())
l = list(map(int, input().split()))

count = [0] * 3
_max_idx = 0
for i, v in enumerate(l):
    idx = i % 3
    count[idx] += v
    if count[idx] > cout[_max_idx]:
        _max_idx = idx
print(['chest', 'biceps', 'back'][_max_idx])