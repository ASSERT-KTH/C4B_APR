n = int(input())
l = list(map(int, input().split()))

count = [0] * 3
_max = 0
_max_idx = 0
for i, v in enumerate(l):
    idx = i % 3
    count[idx] += v
    if count[idx] > _max:
        _max = count[idx]
        _max_idx = idx
print(['chest', 'biceps', 'back'][_max_idx])