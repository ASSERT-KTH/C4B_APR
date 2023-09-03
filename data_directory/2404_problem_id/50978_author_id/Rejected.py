a = []
for i in range(8):
    s = input()
    a.append(s)
k = 0
p = 0
for i in range(8):
    s = a[i]
    if s[0] == 'B':
        k += 1
s = a[0]
for i in range(8):
    if s[i] == 'B':
        p += 1
if k == 8 and p == 8:
    print(8)
else:
    print(k + p)