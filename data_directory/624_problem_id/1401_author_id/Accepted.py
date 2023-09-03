t, s, x = map(int, input().split())
if x < t:
    print("NO")
    exit()
if x == t or (x - t) % s == 0 or ((x - t - 1) % s == 0 and (x - t - 1) // s >= 1):
    print("YES")
else:
    print("NO")