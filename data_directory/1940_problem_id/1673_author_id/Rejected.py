n = int(input().strip())
otvet = 0
for i in range(6,n+1):
    l = []
    for j in range(2,int(i ** 0.5) + 20):
        if i == 1:
            break
        else:
            while i % j == 0:
                i = i // j
                l.append(j)
    if len(set(l)) == 2:
        otvet += 1
print(otvet)