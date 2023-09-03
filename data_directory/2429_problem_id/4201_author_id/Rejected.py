x, y, z, k = map(int, input().split())
sides = sorted([x, y, z])
cuts = 3 * [ None ]
product = 1
for i in reversed(range(3)):
    a = min(sides[i] - 1, k // (i + 1))
    cuts[i] = a
    k -= a
    product *= a + 1
#print(cuts)
print(product)