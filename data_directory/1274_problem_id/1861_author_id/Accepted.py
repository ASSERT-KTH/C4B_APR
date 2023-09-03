p = []
for i in range(4):
    p.append(int(input()))

d = int(input())
h = 0

for i in range(d):
    for j in p:
        if not (i + 1) % j:
            h += 1
            break

print(h)