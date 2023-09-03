import math
n, z = map(int, input().split())
S = []
k = 2
q = round(math.sqrt(n))
while k <= q:
    if n % k == 0:
        S.append(k)
        n //= k
        q = round(math.sqrt(n))
    else:
        k += 1
S.append(n)
s = ""
p = 1
if len(S) < z:
    print(-1)
else:
    if z > 1:
        for a in range(z - 2):
            s += str(S[a]) + " "
        s += str(S[z - 2])
        for b in range(z - 1, len(S)):
            p *= S[b]
        if p > 1:
            s += " " + str(p)
        print(s)
    else:
        print(S[0])