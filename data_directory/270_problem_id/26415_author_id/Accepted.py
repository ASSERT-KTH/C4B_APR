x1, y1, x2, y2 = [int(i) for i in input().split()]
odd = (y2 - y1) // 2 + 1
cnt = (x2 - x1) // 2
print(odd * (x2 - x1 + 1) - cnt)