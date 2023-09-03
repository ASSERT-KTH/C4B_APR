a, b = (int(i) for i in input().split())
print("YES" if abs(a - b) <= 1 else "NO")