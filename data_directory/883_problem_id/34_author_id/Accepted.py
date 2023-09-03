s = input()
d = s + s
l = len(s)
c = set()
for i in range(l):
    aux = d[i:i + l]
    if aux not in c:
        c.add(aux)
print(len(c))