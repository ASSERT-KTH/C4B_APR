n, a, b = map(int, str(input()).strip().split())
print (n - max(a + 1, n - b, 1) + 1)