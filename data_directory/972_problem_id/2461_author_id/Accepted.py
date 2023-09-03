a, b = map(int, input().split())
print('YES' if abs(a - b) <= 1 and max(a, b) > 0 else 'NO')