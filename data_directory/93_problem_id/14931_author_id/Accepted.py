k, a, b = map(int, input().split())
first = a // k * k
if first < a: first += k
last = b // k * k
if last > b: last -= k
# print(first, last)
if last < first:
    print(0)
elif last == first:
    print(1)
else:
    print((last - first) // k + 1)