l = []
for i in range(5):
    l.append(int(input()))

L = [True]*l[4]

for i in l[:4]:
    L[i-1::i] = [False]*len(L[i-1::i])
print(L.count(False))