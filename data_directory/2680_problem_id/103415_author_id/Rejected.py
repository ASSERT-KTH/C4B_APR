a = [int(i) for i in input().split()]
size = a[0]
a = a[1:]
a = sorted(a)
s = [str(x) for x in a]
print(" ".join(s) + (" 100"*10))