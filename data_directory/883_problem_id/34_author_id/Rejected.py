s = input()
d = s + s
l = len(s)
cont = 0
for i in range(l):
    if d[i:i + l] != s:
        cont += 1
print(cont + 1)