import sys

h = sys.stdin.readline().split(' ')
n = sys.stdin.readline().split(' ')

h = [int(i) for i in h]
n = [int(i) for i in n]
d = [h[i] - n[i] for i in range(0,3)]
left = 0
need = 0
for i in range(0,3):
    if d[i] > 0:
        left += d[i]
for i in range(0,3):
    if d[i] < 0:
        need -= d[i]
if left // 2 >= need:
    print('Yes')
else:
    print('No')