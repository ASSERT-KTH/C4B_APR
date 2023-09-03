string = input()
a, b, c = map(int, string.split())
potatoes = []
for x in range(a + 1, c + 1):
    if x % b == 0:
        potatoes.append(x - a)
if len(potatoes) == 0:
    print(-1)
else:
    print(" ".join(map(str, potatoes)))