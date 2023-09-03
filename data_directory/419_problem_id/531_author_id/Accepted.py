'''input
3 2 -100
'''
n, a, b = map(int, input().split())
print((a + b % n) if a + b % n <= n else (a + b % n) % n)