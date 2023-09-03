x1, y1, x2, y2 = [int(i) for i in input().split()]
odd = 0;
even = 0;
if y2 % 2 != 0:
    odd = (y2 - y1) // 2 + 1
    even = (y2 - y1 + 1) // 2;
else:
    odd = (y2 - y1 + 1) // 2
    even = (y2 - y1) // 2 + 1
cnt = (x2 - x1) // 2
print(cnt * (odd + even) + odd * (x1 % 2) + even * (1 - x1 % 2))