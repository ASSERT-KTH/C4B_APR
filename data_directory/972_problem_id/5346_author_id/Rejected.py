a, b = map(int, input().split())
for l in range(1, 111):
    for r in range(l, 111):
        o, e = 0, 0
        for x in range(l, r + 1):
            o += x % 2
            e += 1 - x % 2
        if o == b and e == a:
            print("YES")
            exit()
print("NO")