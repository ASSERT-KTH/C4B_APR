n = int(input())
a = n // 7
for x in range(a + 1):
    if (n - x * 7) % 4 == 0:
        print("4" * ((n - x * 7) // 4) + "7" * x)
        break
else:
    print(-1)