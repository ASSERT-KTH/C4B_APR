a, b, m = map(int, input().split())
if a < b:
    a, b = b, a
for i in range((m + a - 1) // a):
    if (m - a * i) % b == 0 or m - a * i == 0:
        print("Yes")
        exit(0)
print("No")