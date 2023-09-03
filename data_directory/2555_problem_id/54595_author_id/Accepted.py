mx = 0
t = 0
z = 0
for i in input():
    if i == '1':
        t += 1
        z = 0
    else:
        z += 1
        t = 0
    mx = max(mx, z, t)
if mx >= 7:
    print("YES")
else:
    print("NO")