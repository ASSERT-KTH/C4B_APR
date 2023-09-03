c1, c2, ll = [int(x) for x in input().split()]

if c1+c2 < ll:
    c1 += c1+c2
else:
    c1 += ll

print(c1+c2)