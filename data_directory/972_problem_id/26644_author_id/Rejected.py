a, b = map(int, input().split())

print("YES" if a == b + 1 or b == a + 1 or a == b else "NO")