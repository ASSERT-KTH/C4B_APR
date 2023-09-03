p2 = [0, 0, 0, 0]
p1 = [0, 0, 0, 0]
t = False

for i in range(4):
    l, s, r, p = map(int, input().split())
    p1[i] = p
    p2[(i + 1) % 4] += r
    p2[(i - 1) % 4] += l
    p2[(i + 2) % 4] += s
    p2[i] += r + s + l
for i in range(4):
    if p2[i] != 0 and p1[i] != 0:
        t = True

if t:
    print("YES")
else:
    print("NO")