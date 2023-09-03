s = input().split()
n = int(s[0])
m = int(s[1])
k = int(s[-1])
r = (k + 2 * m - 1) // (2 * m)
d = k - (r - 1) * (2 * m)
d = (d + 1) // 2
print(r, d, end = " ")
if k % 2:
    print("L")
else:
    print("R")