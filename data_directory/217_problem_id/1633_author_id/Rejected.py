n = int(input())
a = 0
while a * (a + 1) // 2 < n:
    a += 1
print(n - a * (a - 1) // 2)