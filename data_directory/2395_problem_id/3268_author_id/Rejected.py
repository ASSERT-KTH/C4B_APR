l = list(map(int, input().split()))
a = l.pop(4)
print(max(0, min(l) - a))