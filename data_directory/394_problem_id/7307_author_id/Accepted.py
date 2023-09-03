n, k = (int(i) for i in input().split())
if n == 1:
    print(0)
    exit()
if k >= int(n/2):
    t = n*(n-1)/2
    print(int(t))
    exit()
s = n - 2 * k
p = s*(s-1)/2
l = n*(n-1)/2
output = l - p
print(int(output))