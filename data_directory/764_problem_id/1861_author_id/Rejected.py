l = [int(i) for i in input().split()]
m = sum(l) // 3
print(abs(l[0] - m) + abs(l[1] - m) + abs(l[2] - m))