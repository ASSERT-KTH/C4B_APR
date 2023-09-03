a, b, m = map(int, input().split())
if a < b:
    a, b = b, a
    #print(a, b)
for i in range((m + a) // a):
    if (m - a * i) % b == 0 or m - a * i == 0:
        print("Yes")
        exit(0)
print("No")